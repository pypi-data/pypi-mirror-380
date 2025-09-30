from datetime import datetime, timedelta
import logging
from typing import Optional
import requests
from requests.auth import AuthBase
import stytch
import os


logger = logging.getLogger(__name__)


class StytchAuth(AuthBase):
    def __init__(self, project_id: str, client_id: str, client_secret: str):
        self._project_id = project_id
        self._client_id = client_id
        self._client_secret = client_secret

        self._stytch_client = stytch.Client(
            project_id=project_id,
            secret=client_secret,
            environment="test" if os.getenv("STYTCH_PROJECT_ENV") == "test" else "live",
        )

        self._access_token: Optional[str] = None
        self._access_token_expires_at: Optional[datetime] = None

        self._refresh_buffer_seconds = (
            60  # Refresh the token 60 seconds before it expires
        )

    def __call__(self, r: requests.PreparedRequest) -> requests.PreparedRequest:
        if self._is_token_expired_or_expiring_soon():
            self._auth()

        r.headers["Authorization"] = f"Bearer {self._access_token}"
        return r

    def _auth(self):
        try:
            response = self._stytch_client.m2m.token(
                client_id=self._client_id,
                client_secret=self._client_secret,
            )
        except Exception as e:
            logger.error(f"Failed to authenticate with Stytch: {e}")
            raise

        self._access_token_expires_at = datetime.now() + timedelta(
            seconds=response.expires_in
        )
        self._access_token = response.access_token

        logger.info(
            "Obtained new Stytch access token for project %s, expires at %s",
            self._project_id,
            self._access_token_expires_at,
        )

    def _is_token_expired_or_expiring_soon(self) -> bool:
        if self._access_token is None or self._access_token_expires_at is None:
            return True
        buffer_time = datetime.now() + timedelta(seconds=self._refresh_buffer_seconds)
        return self._access_token_expires_at <= buffer_time
