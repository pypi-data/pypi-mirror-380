import dotenv

from anzar._api.jwt_interceptor import JwtInterceptor
from anzar._api.session_interceptor import SessionInterceptor
from anzar._auth.authenticator import AuthManager
from anzar._models.anzar_config import (
    AnzarConfig,
    AuthStrategy,
    Authentication,
    Database,
    DatabaseDriver,
    EmailAndPassword,
)

from ._api.client import HttpClient

_ = dotenv.load_dotenv()


default_config = AnzarConfig(
    api_url="http://localhost:3000",
    database=Database(
        connection_string="sqlite:memory:",
        driver=DatabaseDriver.SQLite,
    ),
    auth=Authentication(
        strategy=AuthStrategy.Session,
    ),
    emailAndPassword=EmailAndPassword(
        enable=True,
    ),
)


def AnzarAuth(config: AnzarConfig = default_config) -> AuthManager:
    http_interceptor = (
        SessionInterceptor()
        if config.auth.strategy == AuthStrategy.Session
        else JwtInterceptor()
    )
    return AuthManager(
        HttpClient(
            http_interceptor,
        ),
        config,
    )


__all__ = ["AnzarAuth"]
