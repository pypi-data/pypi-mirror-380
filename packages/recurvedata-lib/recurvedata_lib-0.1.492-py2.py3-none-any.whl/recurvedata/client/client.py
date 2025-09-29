import json
import logging
import os
import time
from pathlib import Path
from typing import Any, TypeVar, overload

import httpx
from pydantic import BaseModel

from recurvedata.__version__ import __version__
from recurvedata.config import AgentConfig
from recurvedata.exceptions import APIError, MaxRetriesExceededException, UnauthorizedError

logger = logging.getLogger(__name__)

ResponseModelType = TypeVar("ResponseModelType", bound=BaseModel)


class Client:
    _config: AgentConfig
    _client: httpx.Client

    def __init__(self, config: AgentConfig = None):
        if not config:
            config = AgentConfig.load()
        self.set_config(config)

    @property
    def is_offline_mode(self) -> bool:
        """Check if offline mode is enabled via environment variable"""
        return os.environ.get("RECURVE_OFFLINE_MODE", "").lower() in ("true", "1")

    @property
    def offline_data_path(self) -> Path:
        """Get the offline data directory path"""
        offline_path = os.environ.get("RECURVE_OFFLINE_DATA_PATH", "offline_data")
        return Path(offline_path)

    def set_config(self, config: AgentConfig):
        self._config = config
        # Only create HTTP client if not in offline mode
        if not self.is_offline_mode:
            self._client = httpx.Client(
                base_url=config.server_url,
                timeout=config.request_timeout,
                headers={"User-Agent": f"RecurveLib/{__version__}"},
            )
        else:
            self._client = None

    def _resolve_offline_file_path(self, path: str, **kwargs) -> Path:
        """Convert API path to local file path with parameterized support"""
        # Remove leading /api/ prefix: /api/executor/connection -> executor/connection
        if path.startswith("/api/"):
            clean_path = path[5:]  # Remove "/api/" prefix
        else:
            clean_path = path.lstrip("/")
        
        # Extract parameters from kwargs
        params = kwargs.get("params", {})
        
        # CORE OPERATOR APIs with parameter-based file structure:
        
        # 1. get_connection() API - parameterized by project_id + connection_name
        if clean_path == "executor/connection":
            project_id = params.get("project_id", "0")
            connection_name = params.get("name", "default")
            return self.offline_data_path / "executor/connection" / str(project_id) / f"{connection_name}.json"
            
        # 2. get_py_conn_configs() API - parameterized by project_id + project_connection_name  
        elif clean_path == "executor/python-conn-configs":
            project_id = params.get("project_id", "0")
            # Python configs use project_connection_name as the key (fallback to other param names for compatibility)
            # Handle empty strings properly - treat them as None/missing
            project_connection_name = (params.get("project_connection_name") or 
                                     params.get("project_conn_name") or 
                                     params.get("pyenv_name") or 
                                     "default")
            return self.offline_data_path / "executor/python-conn-configs" / str(project_id) / f"{project_connection_name}.json"
        
        # For any other APIs, raise error do not support offline mode
        raise APIError(f"Offline mode: {path} is not supported")

    def _read_offline_data(self, method: str, path: str, response_model_class: type[ResponseModelType] | None = None, **kwargs) -> Any:
        """Read API response from local JSON file"""
        file_path = self._resolve_offline_file_path(path, **kwargs)
        
        logger.info(f"🔌 Offline mode: Reading from {file_path}")
        
        try:
            if not file_path.exists():
                logger.error(f"Offline data file not found: {file_path}")
                raise APIError(f"Offline mode: Required data file not found: {file_path}")
            
            with open(file_path, 'r') as f:
                resp_content = json.load(f)
            
            # Handle response model validation (same logic as online mode)
            if response_model_class is not None:
                if "code" in resp_content:
                    return response_model_class.model_validate(resp_content["data"])
                return response_model_class.model_validate(resp_content)
            
            return resp_content.get("data", resp_content)
            
        except APIError:
            raise  # Re-raise APIError as-is
        except Exception as e:
            logger.error(f"Error reading offline data from {file_path}: {e}")
            raise APIError(f"Offline mode: Failed to read data file {file_path}: {e}")


    @overload
    def request(self, method: str, path: str, response_model_class: None = None, retries: int = 3, **kwargs) -> Any:
        ...

    @overload
    def request(
        self, method: str, path: str, response_model_class: type[ResponseModelType], retries: int = 3, **kwargs
    ) -> ResponseModelType:
        ...

    def prepare_header(self, kwargs: dict):
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self._config.agent_id}:{self._config.token.get_secret_value()}"
        headers["X-Tenant-Domain"] = self._config.tenant_domain
        kwargs["headers"] = headers

    def request(
        self,
        method: str,
        path: str,
        response_model_class: type[ResponseModelType] | None = None,
        retries: int = 1,
        **kwargs,
    ) -> Any:
        # Route to offline mode if enabled
        if self.is_offline_mode:
            return self._read_offline_data(method, path, response_model_class, **kwargs)
        
        # Original online mode logic
        self.prepare_header(kwargs)
        pre_err: httpx.HTTPStatusError | None = None
        for attempt in range(retries):
            try:
                resp = self._client.request(method, path, **kwargs)
                resp.raise_for_status()
                resp_content = resp.json()

                # TODO(yangliang): handle errors more gracefully
                if "code" in resp_content and resp_content["code"] != "0":
                    raise APIError(f"API request failed: {resp_content['msg']}\n{resp_content.get('data')}")

                if response_model_class is not None:
                    if "code" in resp_content:
                        return response_model_class.model_validate(resp_content["data"])
                    return response_model_class.model_validate(resp_content)
                return resp_content.get("data")
            except httpx.HTTPStatusError as e:
                pre_err = e
                logger.error(
                    f"HTTP error on attempt {attempt + 1} for url '{e.request.url}' :"
                    f" {e.response.status_code} - {e.response.text}"
                )
                if e.response.status_code == 401:
                    raise UnauthorizedError("Unauthorized, please check your agent_id and token")
            except httpx.RequestError as e:
                logger.debug(f"Request error on attempt {attempt + 1} for url '{e.request.url}': {e}")

            if attempt < retries - 1:
                time.sleep(2**attempt)  # Exponential backoff
            else:
                err_msg = str(pre_err) if pre_err else ""
                raise MaxRetriesExceededException(
                    f"Failed to complete {method} request to {path} after {retries} attempts, {err_msg}"
                )

    def request_file(
        self,
        method: str,
        path: str,
        file_name: str,
        retries: int = 1,
        **kwargs,
    ) -> bool:
        self.prepare_header(kwargs)

        pre_err: httpx.HTTPStatusError | None = None
        for attempt in range(retries):
            try:
                resp = self._client.request(method, path, **kwargs)
                resp.raise_for_status()
                try:
                    resp_content = resp.json()

                    if "code" in resp_content and resp_content["code"] != "0":
                        raise APIError(f"API request failed: {resp_content['msg']}\n{resp_content.get('data')}")
                except (json.JSONDecodeError, TypeError, UnicodeDecodeError):
                    pass

                if not resp.content:
                    return False

                with open(file_name, "wb") as f:
                    f.write(resp.content)
                return True

                # TODO(yangliang): handle errors more gracefully
            except httpx.HTTPStatusError as e:
                logger.debug(
                    f"HTTP error on attempt {attempt + 1} for url '{e.request.url}' :"
                    f" {e.response.status_code} - {e.response.text}"
                )
                pre_err = e
                if e.response.status_code == 401:
                    raise UnauthorizedError("Unauthorized, please check your agent_id and token")
            except httpx.RequestError as e:
                logger.debug(f"Request error on attempt {attempt + 1} for url '{e.request.url}': {e}")

            if attempt < retries - 1:
                time.sleep(2**attempt)  # Exponential backoff
            else:
                err_msg = str(pre_err) if pre_err else ""
                raise MaxRetriesExceededException(
                    f"Failed to complete {method} request to {path} after {retries} attempts {err_msg}"
                )

    def close(self):
        if self._client:
            self._client.close()

    @property
    def base_url(self) -> str:
        if self.is_offline_mode:
            return "offline://localhost"
        return str(self._client.base_url) if self._client else ""
