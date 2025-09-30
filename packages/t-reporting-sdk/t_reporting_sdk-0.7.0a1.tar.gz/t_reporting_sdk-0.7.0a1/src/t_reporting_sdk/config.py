import os
from typing import Optional
from enum import Enum

from t_reporting_sdk.repositories.api_clients.fabric.client import FabricClientConfig


class Backend(Enum):
    FABRIC = "fabric"
    THOUGHTHUB = "thoughthub"


class ReportingSDKConfig:
    """Singleton configuration class for the SDK."""

    _instance: Optional["ReportingSDKConfig"] = None

    backend: Backend

    fabric_client_config: FabricClientConfig

    # Thoughthub backend
    agent_performance_tracking_url: Optional[str] = None
    stytch_project_id: Optional[str] = None
    stytch_client_id: Optional[str] = None
    stytch_client_secret: Optional[str] = None

    def __new__(cls) -> "ReportingSDKConfig":
        """Singleton instance creation."""
        if cls._instance is None:
            # The super() function here refers to the base (object) class, which is the default parent of all Python classes.
            # Calling super().__new__(cls) invokes the object class's __new__ method to allocate memory for a new instance.
            # This is crucial for the singleton pattern, as it ensures proper instance creation and allows us to enforce
            # that only one instance of the class is ever created. The intent of this code is to control object creation
            # and reuse a single shared instance across the application.
            cls._instance = super().__new__(cls)
            # This ensures that the config is always initialized with values
            cls._instance.configure()
        return cls._instance

    @classmethod
    def configure(
        cls,
        *,
        backend: Backend = Backend.FABRIC,
        fabric_base_url: Optional[str] = None,
        fabric_user_email: Optional[str] = None,
        fabric_user_secret: Optional[str] = None,
        agent_performance_tracking_url: Optional[str] = None,
        stytch_project_id: Optional[str] = None,
        stytch_client_id: Optional[str] = None,
        stytch_client_secret: Optional[str] = None,
    ) -> "ReportingSDKConfig":
        """Set the configuration for the SDK."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        cls._instance.backend = backend

        if cls._instance.backend == Backend.FABRIC:
            fabric_base_url = fabric_base_url or os.getenv("FABRIC_BASE_URL")
            fabric_user_email = fabric_user_email or os.getenv("FABRIC_USER_EMAIL")
            fabric_user_secret = fabric_user_secret or os.getenv(
                "FABRIC_USER_OTP_SECRET"
            )

            if not all([fabric_base_url, fabric_user_email, fabric_user_secret]):
                raise ValueError(
                    "Fabric client configuration must be fully provided for FABRIC backend."
                )

            cls._instance.fabric_client_config = FabricClientConfig(
                base_url=fabric_base_url,  # type: ignore
                user_email=fabric_user_email,  # type: ignore
                user_otp_secret=fabric_user_secret,  # type: ignore
            )
        elif cls._instance.backend == Backend.THOUGHTHUB:
            cls._instance.agent_performance_tracking_url = (
                agent_performance_tracking_url
                or os.getenv("AGENT_PERFORMANCE_TRACKING_URL")
            )
            cls._instance.stytch_project_id = stytch_project_id or os.getenv(
                "STYTCH_PROJECT_ID"
            )
            cls._instance.stytch_client_id = stytch_client_id or os.getenv(
                "STYTCH_CLIENT_ID"
            )
            cls._instance.stytch_client_secret = stytch_client_secret or os.getenv(
                "STYTCH_CLIENT_SECRET"
            )
            if not all(
                [
                    cls._instance.agent_performance_tracking_url,
                    cls._instance.stytch_project_id,
                    cls._instance.stytch_client_id,
                    cls._instance.stytch_client_secret,
                ]
            ):
                raise ValueError(
                    "Stytch credentials must be provided for THOUGHTHUB backend."
                )

        return cls._instance
