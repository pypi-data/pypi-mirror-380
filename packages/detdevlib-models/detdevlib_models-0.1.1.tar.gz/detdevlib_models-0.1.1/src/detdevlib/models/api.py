# packages/detdevlib-models/src/detdevlib/models/api.py

import json
import logging
import os
from datetime import datetime
from io import BytesIO
from typing import Any, Callable, Type, TypeVar

import httpx
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from fastapi import BackgroundTasks, FastAPI, Response, status
from pydantic import BaseModel, create_model

FILENAME_PLACEHOLDER = "__PLACEHOLDER_FILENAME__"
logger = logging.getLogger(__name__)
ModelSettings = TypeVar("ModelSettings", bound=BaseModel)


class OutputModel(BaseModel):
    """A structured object for defining a single output file."""

    data: Any
    filename: str
    file_type: str
    path: str = ""


class OutputFileHandler:
    """Class to handle output files for a model"""

    def __init__(self) -> None:
        self.base_path = os.path.join("outputs", datetime.now().strftime("%H_%M_%S"))

        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def get_model_outputs(self) -> list[OutputModel]:
        """
        Get the model outputs as a list of OutputModel instances.
        """
        output_files = []
        for root, _, files in os.walk(self.base_path):

            for file in files:
                file_type = file.split(".")[-1]
                file_data = self.read_data(os.path.join(root, file), file_type)
                output = OutputModel(
                    data=file_data,
                    filename=file,
                    file_type=file_type,
                    path=root,
                )
                output_files.append(output)
        return output_files

    def delete_output_dir(self) -> None:
        """
        Delete the output directory and all its contents
        """
        if os.path.exists(self.base_path):
            for root, dirs, files in os.walk(self.base_path, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for directory in dirs:
                    os.rmdir(os.path.join(root, directory))
            os.rmdir(self.base_path)

    @staticmethod
    def split_away_first_dir(path: str) -> str:
        """Remove the first directory from the file path."""
        parts = path.split(os.sep)
        if len(parts) > 1:
            return os.sep.join(parts[1:])
        return path

    @staticmethod
    def read_data(path: str, type: str) -> any:
        """
        Read data from a file based on its type

        Returns:
            any: The data read from the file
        """
        if type == "csv":
            return pd.read_csv(path)
        elif type == "json":
            with open(path, "r") as f:
                return json.load(f)
        elif type == "html":
            with open(path, "r") as f:
                return f.read()
        elif type == "npz":
            with np.load(path) as data:
                return data["data"]
        raise NotImplementedError(f"File type {type} is not supported")


def _serialize(output: OutputModel) -> bytes:
    """Get the raw payload bytes"""
    if output.file_type == "csv" and isinstance(output.data, pd.DataFrame):
        return output.data.to_csv(index=False).encode("utf-8")
    if output.file_type == "json" and isinstance(output.data, dict):
        return json.dumps(output.data, indent=2).encode("utf-8")
    if output.file_type == "html" and isinstance(output.data, go.Figure):
        return output.data.to_html().encode("utf-8")
    if output.file_type == "npz" and isinstance(output.data, np.ndarray):
        buffer = BytesIO()
        np.savez_compressed(buffer, data=output.data)  # type: ignore
        buffer.seek(0)
        return buffer.read()
    raise NotImplementedError(
        f"combination of data type {type(output.data)} and file_type ({output.file_type}) is not supported"
    )


def _serialize_and_upload(sas_url: str, output: OutputModel) -> None:
    """Helper method to serialize data based on type and upload it to blob storage"""
    # Serialize the output
    payload = _serialize(output)

    # Construct the full path and upload
    relative_path = f"{output.path.strip('/')}/" if output.path else ""
    full_filename = f"{relative_path}{output.filename}.{output.file_type}"
    if FILENAME_PLACEHOLDER not in sas_url:
        raise ValueError(
            f"sas_url {sas_url} is missing filename placeholder {FILENAME_PLACEHOLDER}"
        )
    final_url = sas_url.replace(FILENAME_PLACEHOLDER, full_filename)

    # Use requests for clarity, similar to the old implementation
    response = httpx.put(final_url, content=payload, headers={"x-ms-blob-type": "BlockBlob"})
    response.raise_for_status()


def create_model_api(
    model_function: Callable[[ModelSettings], list[OutputModel]],
    settings_class: Type[ModelSettings],
    endpoint_path: str,
):
    """Factory to create a FastAPI app that handles model execution and output uploads."""
    app = FastAPI(title=model_function.__name__)

    ConfigModel = create_model(
        "ConfigModel",
        task_id=(str, ...),
        output_sas_url=(str, ...),
        callback_url=(str, ...),
        model_settings=(settings_class, ...),
    )

    def _run_task_and_callback(config: ConfigModel):
        """Internal wrapper that runs the model, uploads the result, and handles callbacks."""
        try:
            output_items = model_function(config.model_settings)

            for item in output_items:
                _serialize_and_upload(config.output_sas_url, item)

            message = f"Task finished. {len(output_items)} file(s) created."
            status = "COMPLETED"
        except Exception as e:
            message = f"An error occurred: {e}"
            status = "FAILED"

        callback_data = {"task_id": config.task_id, "status": status, "message": message}
        try:
            response = httpx.post(config.callback_url, json=callback_data)
            response.raise_for_status()
        except httpx.RequestError as e:
            # This catches network errors (e.g., connection refused, DNS failure)
            logger.warning(
                f"Callback for task {config.task_id} failed. Could not connect to {e.request.url!r}."
            )
        except httpx.HTTPStatusError as e:
            # This catches non-2xx server responses
            logger.warning(
                f"Callback for task {config.task_id} received an error response "
                f"{e.response.status_code} from server: {e.response.text}"
            )

    @app.post(endpoint_path, description=model_function.__doc__)
    async def main_endpoint(config: ConfigModel, background_tasks: BackgroundTasks):
        """Starts the model asynchronously, and respond with 202 to signal tasks have been started."""
        background_tasks.add_task(_run_task_and_callback, config)
        return Response(status_code=status.HTTP_202_ACCEPTED)

    @app.get("/healthcheck")
    async def healthcheck():
        """Used to verify if the app is available."""
        return {"status": "ok"}

    return app
