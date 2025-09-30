from typing import Any

from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass(slots=True)
class BaseUser:
    id: str
    email: str | None
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class BaseAuthToken:
    access_token: str
    refresh_token: str | None = field(default=None)
    token_type: str = field(default="bearer")
    expires_in: int | None = field(default=None)  # in seconds


class BaseUserValidator(ABC):
    @abstractmethod
    async def validate_credentials(
        self, email: str, password: str
    ) -> dict[str, Any] | None: ...
    @abstractmethod
    async def create_user(self, details: dict[str, Any]) -> dict[str, Any]: ...


class BaseAuthProtocol(ABC):
    @abstractmethod
    async def register(self, details: dict[str, Any]) -> BaseUser: ...
    @abstractmethod
    async def login(self, credentials: dict[str, Any]) -> BaseAuthToken: ...
    @abstractmethod
    async def logout(self, token: str) -> None: ...
    @abstractmethod
    async def get_user(self, token: str) -> BaseUser | None: ...
    @abstractmethod
    async def refresh_token(self, refresh_token: str) -> BaseAuthToken: ...
