import logging
from datetime import datetime
from typing import Any, Dict

import jwt
from boltons.cacheutils import cachedproperty
from requests import PreparedRequest
from requests.auth import AuthBase

from DKCommon.dt_utils import timestamp_to_utc, utcnow

from .settings import DEFAULT_JWT_OPTIONS

LOG = logging.getLogger(__name__)


class HeaderAuth(AuthBase):
    """Base class for Header-based authentication for Requests sessions."""

    def __init__(self, token: str, token_prefix: str = "Bearer"):
        self.token = token
        self.token_prefix = token_prefix
        self.key = "Authorization"
        self.value = " ".join((token_prefix, token))

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        r.headers[self.key] = self.value
        return r

    refreshable = False


class JWTHeaderAuth(HeaderAuth):
    """Header-based JWT authentication for Requests sessions."""

    refreshable = True

    @cachedproperty
    def claims(self) -> Dict[str, Any]:
        return jwt.decode(self.token, options=DEFAULT_JWT_OPTIONS)

    @cachedproperty
    def unverified_claims(self) -> Dict[str, Any]:
        return self.claims  # All our claims are "unverified" but requests wants both

    @property
    def expiration(self) -> datetime:
        """Returns the token expiration as a datetime object."""
        try:
            return timestamp_to_utc(self.claims["exp"])
        except KeyError:
            raise Exception("Token claims missing `exp` key")
        except Exception:
            raise ValueError(f"Unable to parse expiration from `{self.claims['exp']}`")

    @property
    def expired(self) -> bool:
        """Check to see if the token is expired."""
        return self.expiration < utcnow()

    @property
    def expire_seconds(self) -> int:
        """Number of seconds until this token expires."""
        if self.expired:
            return 0
        delta = self.expiration - utcnow()
        seconds = int(delta.total_seconds())
        if seconds > 0:
            return seconds
        else:
            return 0


class JobHeaderAuth(HeaderAuth):
    """Header-based apitoken authentication for Requests sessions"""

    @cachedproperty
    def claims(self) -> Dict[str, Any]:
        return {}

    @cachedproperty
    def unverified_claims(self) -> Dict[str, Any]:
        return self.claims  # Simple alias


def get_auth_instance(token: str) -> AuthBase:
    try:
        jwt.decode(token, options=DEFAULT_JWT_OPTIONS)
    except jwt.DecodeError:
        return JobHeaderAuth(token)
    else:
        return JWTHeaderAuth(token)
