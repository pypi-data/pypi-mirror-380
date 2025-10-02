"""Environment Setup."""

from __future__ import annotations

import os
import ssl
from typing import Optional

from pydantic.v1 import BaseSettings, Field

from .core_config import get_logger


class EnvironmentConfig(BaseSettings):
    """Basic Configuration for definition environment."""

    def __hash__(self):
        return hash((type(self), *tuple(self.__dict__.values())))

    name: str
    web_api_endpoint: str
    website_endpoint: str
    s3_region: str
    ssl_verify: bool = Field(True, env="TIDY3D_SSL_VERIFY")
    enable_caching: Optional[bool] = None
    ssl_version: Optional[ssl.TLSVersion] = None
    env_vars: Optional[dict[str, str]] = None

    def active(self) -> None:
        """Activate the environment instance."""
        Env.set_current(self)

    def get_real_url(self, path: str) -> str:
        """Get the real url for the environment instance.

        Parameters
        ----------
        path : str
            Base path to append to web api endpoint.

        Returns
        -------
        str
            Full url for the webapi.
        """
        return "/".join([self.web_api_endpoint, path])


dev = EnvironmentConfig(
    name="dev",
    s3_region="us-east-1",
    web_api_endpoint="https://tidy3d-api.dev-simulation.cloud",
    website_endpoint="https://tidy3d.dev-simulation.cloud",
)

uat = EnvironmentConfig(
    name="uat",
    s3_region="us-west-2",
    web_api_endpoint="https://tidy3d-api.uat-simulation.cloud",
    website_endpoint="https://tidy3d.uat-simulation.cloud",
)

pre = EnvironmentConfig(
    name="pre",
    s3_region="us-gov-west-1",
    web_api_endpoint="https://preprod-tidy3d-api.simulation.cloud",
    website_endpoint="https://preprod-tidy3d.simulation.cloud",
)

prod = EnvironmentConfig(
    name="prod",
    s3_region="us-gov-west-1",
    web_api_endpoint="https://tidy3d-api.simulation.cloud",
    website_endpoint="https://tidy3d.simulation.cloud",
)


nexus = EnvironmentConfig(
    name="nexus",
    web_api_endpoint="http://127.0.0.1:5000",
    ssl_verify=False,
    enable_caching=False,
    s3_region="us-east-1",
    website_endpoint="http://127.0.0.1/tidy3d",
    env_vars={"AWS_ENDPOINT_URL_S3": "http://127.0.0.1:9000"},
)


class Environment:
    """Environment decorator for user interactive.

    Example
    -------
    >>> from tidy3d.web.core.environment import Env
    >>> Env.dev.active()
    >>> assert Env.current.name == "dev"
    ...
    """

    env_map = {
        "dev": dev,
        "uat": uat,
        "prod": prod,
        "nexus": nexus,
    }

    def __init__(self):
        log = get_logger()
        """Initialize the environment."""
        self._previous_env_vars = {}
        env_key = os.environ.get("TIDY3D_ENV")
        env_key = env_key.lower() if env_key else env_key
        log.info(f"env_key is {env_key}")
        if not env_key:
            self._current = prod
        elif env_key in self.env_map:
            self._current = self.env_map[env_key]
        else:
            log.warning(
                f"The value '{env_key}' for the environment variable TIDY3D_ENV is not supported. "
                f"Using prod as default."
            )
            self._current = prod

        if self._current.env_vars:
            for key, value in self._current.env_vars.items():
                self._previous_env_vars[key] = os.environ.get(key)
                os.environ[key] = value

    @property
    def current(self) -> EnvironmentConfig:
        """Get the current environment.

        Returns
        -------
        EnvironmentConfig
            The config for the current environment.
        """
        return self._current

    @property
    def dev(self) -> EnvironmentConfig:
        """Get the dev environment.

        Returns
        -------
        EnvironmentConfig
            The config for the dev environment.
        """
        return dev

    @property
    def uat(self) -> EnvironmentConfig:
        """Get the uat environment.

        Returns
        -------
        EnvironmentConfig
            The config for the uat environment.
        """
        return uat

    @property
    def pre(self) -> EnvironmentConfig:
        """Get the preprod environment.

        Returns
        -------
        EnvironmentConfig
            The config for the preprod environment.
        """
        return pre

    @property
    def prod(self) -> EnvironmentConfig:
        """Get the prod environment.

        Returns
        -------
        EnvironmentConfig
            The config for the prod environment.
        """
        return prod

    @property
    def nexus(self) -> EnvironmentConfig:
        """Get the nexus environment.

        Returns
        -------
        EnvironmentConfig
            The config for the nexus environment.
        """
        return nexus

    def set_current(self, config: EnvironmentConfig) -> None:
        """Set the current environment.

        Parameters
        ----------
        config : EnvironmentConfig
            The environment to set to current.
        """
        for key, value in self._previous_env_vars.items():
            if value is None:
                if key in os.environ:
                    del os.environ[key]
            else:
                os.environ[key] = value
        self._previous_env_vars = {}

        if config.env_vars:
            for key, value in config.env_vars.items():
                self._previous_env_vars[key] = os.environ.get(key)
                os.environ[key] = value

        self._current = config

    def enable_caching(self, enable_caching: bool = True) -> None:
        """Set the environment configuration setting with regards to caching simulation results.

        Parameters
        ----------
        enable_caching: bool = True
            If ``True``, do duplicate checking. Return the previous simulation result if duplicate simulation is found.
            If ``False``, do not duplicate checking. Just run the task directly.
        """
        self._current.enable_caching = enable_caching

    def set_ssl_version(self, ssl_version: ssl.TLSVersion) -> None:
        """Set the ssl version.

        Parameters
        ----------
        ssl_version : ssl.TLSVersion
            The ssl version to set.
        """
        self._current.ssl_version = ssl_version


Env = Environment()
