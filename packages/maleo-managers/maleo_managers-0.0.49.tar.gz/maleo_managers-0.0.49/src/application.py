from abc import ABC, abstractmethod
from google.oauth2.service_account import Credentials
from typing import Generic
from maleo.enums.environment import Environment
from maleo.enums.service import Key
from maleo.schemas.application import ApplicationSettingsT, ApplicationContext
from maleo.logging.config import Config as LogConfig
from maleo.logging.logger import ServiceLoggers
from .config import ConfigT


class ApplicationManager(ABC, Generic[ApplicationSettingsT, ConfigT]):
    """ApplicationManager class"""

    def __init__(
        self,
        google_credentials: Credentials,
        log_config: LogConfig,
        settings: ApplicationSettingsT,
        config: ConfigT,
    ):
        self._google_credentials = google_credentials
        self._log_config = log_config
        self._settings = settings
        self._config = config

        self._application_context = ApplicationContext.from_settings(settings)

        self._initialize_loggers()

    def _initialize_loggers(self) -> None:
        self.loggers = ServiceLoggers[Environment, Key].new(
            environment=self._settings.ENVIRONMENT,
            service_key=self._settings.SERVICE_KEY,
            config=self._log_config,
        )

    @abstractmethod
    def _initialize_database(self):
        """Initialize all given databases"""

    @abstractmethod
    def _initialize_google_cloud_storage(self):
        """Initialize Google Cloud Storage"""
