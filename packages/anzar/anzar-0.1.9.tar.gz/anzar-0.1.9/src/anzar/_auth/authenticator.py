import os
import sys

from anzar._api.client import HttpClient
from anzar._models.anzar_config import AnzarConfig
from anzar._models.auth import AuthResponse
from anzar._models.user import User
from anzar._utils.context import ContextModel
from anzar._utils.errors import Error
from anzar._utils.storage import TokenStorage
from anzar._utils.types import NoType, TokenType
from anzar._utils.validator import Validator


class AuthManager:
    def __init__(self, httpClient: HttpClient, config: AnzarConfig) -> None:
        self._http_client: HttpClient = httpClient

        self._API_URL: str = os.getenv("API_URL", "http://localhost:3000")
        assert self._API_URL is not None, "Env was unable to load"

        self.__endpoints: dict[str, str] = {
            "context": f"{self._API_URL}/configuration/register_context",
            "health_check": f"{self._API_URL}/health_check",
            "login": f"{self._API_URL}/auth/login",
            "register": f"{self._API_URL}/auth/register",
            "user": f"{self._API_URL}/user",
            "logout": f"{self._API_URL}/auth/logout",
        }

        response = self._register_context(config)
        if isinstance(response, Error):
            sys.exit(response.message)
        self._health_check()

    def _register_context(self, config: AnzarConfig) -> Error | ContextModel:
        url = self.__endpoints["context"]
        return self._http_client.post(url, config, ContextModel)

    def _health_check(self):
        try:
            url = self.__endpoints["health_check"]
            _ = self._http_client.health_check(url)
        except ConnectionError as _:
            sys.exit(1)

    def register(self, username: str, email: str, password: str) -> Error | User:
        req = Validator().construct_register(username, email, password)
        if isinstance(req, Error):
            return req

        url = self.__endpoints["register"]
        response = self._http_client.post(url, req, AuthResponse)

        return response.user if isinstance(response, AuthResponse) else response

    def login(self, email: str, password: str):
        req = Validator().construct_login(email, password)
        if isinstance(req, Error):
            return req

        url = self.__endpoints["login"]
        response = self._http_client.post(url, req, AuthResponse)

        return response.user if isinstance(response, AuthResponse) else response

    def logout(self):
        url = self.__endpoints["logout"]
        response = self._http_client.post(url, None, NoType)

        return response

    def getSession(self):
        url = self.__endpoints["user"]
        response = self._http_client.get(url, User)

        # FIXME
        # load session not sessionID
        session = TokenStorage().load(TokenType.SessionToken.name)

        if isinstance(response, Error):
            return response

        return {"session": session, "response": response}

    def isLoggedIn(self):
        return TokenStorage().load(TokenType.AccessToken.name) is not None
