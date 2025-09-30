import os
from dotenv import load_dotenv
from enum import StrEnum
from pathlib import Path
from pydantic import BaseModel, Field, model_validator
from pydantic_settings import BaseSettings
from typing import Annotated, Optional, Self, TypeVar
from maleo.enums.environment import Environment
from maleo.enums.service import Key, Name
from maleo.types.string import ListOfStrings, OptionalString


class Execution(StrEnum):
    CONTAINER = "container"
    DIRECT = "direct"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


class ApplicationContext(BaseModel):
    environment: Annotated[
        Environment, Field(..., description="Application's environment")
    ]
    key: Annotated[Key, Field(..., description="Application's key")]

    @classmethod
    def from_env(cls) -> "ApplicationContext":
        load_dotenv()
        environment = os.getenv("ENVIRONMENT", None)
        if environment is None:
            raise ValueError("Variable 'ENVIRONMENT' not found in ENV")

        key = os.getenv("SERVICE_KEY", None)
        if key is None:
            raise ValueError("Variable 'SERVICE_KEY' not found in ENV")

        return cls(environment=Environment(environment), key=Key(key))

    @classmethod
    def from_settings(cls, settings: "ApplicationSettings") -> "ApplicationContext":
        return cls(environment=settings.ENVIRONMENT, key=settings.SERVICE_KEY)


OptionalApplicationContext = Optional[ApplicationContext]


class ApplicationContextMixin(BaseModel):
    application_context: Annotated[
        ApplicationContext,
        Field(ApplicationContext.from_env(), description="Application's context"),
    ] = ApplicationContext.from_env()


class ApplicationSettings(BaseSettings):
    EXECUTION: Annotated[
        Execution, Field(Execution.CONTAINER, description="Execution mode")
    ] = Execution.CONTAINER

    ENVIRONMENT: Annotated[Environment, Field(..., description="Environment")]

    HOST: Annotated[str, Field("127.0.0.1", description="Application's host")] = (
        "127.0.0.1"
    )
    PORT: Annotated[int, Field(8000, description="Application's port")] = 8000
    HOST_PORT: Annotated[int, Field(8000, description="Host's port")] = 8000
    DOCKER_NETWORK: Annotated[
        str, Field("maleo-suite", description="Docker's network")
    ] = "maleo-suite"
    SERVICE_KEY: Annotated[Key, Field(..., description="Application's key")]
    SERVICE_NAME: Annotated[Name, Field(..., description="Application's name")]
    ROOT_PATH: Annotated[str, Field("", description="Application's root path")] = ""

    GOOGLE_APPLICATION_CREDENTIALS: Annotated[
        str,
        Field(
            "/etc/maleo/credentials/google-service-account.json",
            description="Google application credential's file path",
        ),
    ] = "/etc/maleo/credentials/google-service-account.json"

    USE_LOCAL_CONFIG: Annotated[
        bool, Field(False, description="Whether to use local config")
    ] = False
    CONFIG_PATH: Annotated[OptionalString, Field(None, description="Config path")] = (
        None
    )
    KEY_PASSWORD: Annotated[
        OptionalString, Field(None, description="Key's password")
    ] = None
    PRIVATE_KEY: Annotated[OptionalString, Field(None, description="Private key")] = (
        None
    )
    PUBLIC_KEY: Annotated[OptionalString, Field(None, description="Public key")] = None

    @model_validator(mode="after")
    def validate_config_path(self) -> Self:
        if self.USE_LOCAL_CONFIG:
            if self.CONFIG_PATH is None:
                self.CONFIG_PATH = (
                    f"/etc/maleo/config/{self.SERVICE_KEY}/{self.ENVIRONMENT}.yaml"
                )
            config_path = Path(self.CONFIG_PATH)
            if not config_path.exists() or not config_path.is_file():
                raise ValueError(
                    f"Config path '{self.CONFIG_PATH}' either did not exist or is not a file"
                )

        return self

    @property
    def context(self) -> ApplicationContext:
        return ApplicationContext(environment=self.ENVIRONMENT, key=self.SERVICE_KEY)


ApplicationSettingsT = TypeVar("ApplicationSettingsT", bound=ApplicationSettings)
