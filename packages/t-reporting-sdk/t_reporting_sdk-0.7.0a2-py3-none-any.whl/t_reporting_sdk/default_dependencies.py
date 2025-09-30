import logging
from t_reporting_sdk.repositories.agent_runs.repository import AgentRunsRepository
from t_reporting_sdk.repositories.api_clients.agent_performance_tracking.agent_performance_tracking import (
    AgentPerformanceTrackingClient,
)
from t_reporting_sdk.repositories.api_clients.fabric.client import FabricClient
from t_reporting_sdk.repositories.eva_records.repository import EVARecordsRepository
from t_reporting_sdk.repositories.cam_records.repository import CAMRecordsRepository
from t_reporting_sdk.repositories.paula_records.repository import PAULARecordsRepository
from t_reporting_sdk.config import Backend, ReportingSDKConfig

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sdk_config = ReportingSDKConfig()
if sdk_config.backend == Backend.FABRIC:
    logger.info("Using FABRIC backend")
    client = FabricClient(config=sdk_config.fabric_client_config)
else:
    logger.info("Using THOUGHTHUB backend")
    client = AgentPerformanceTrackingClient(
        url=sdk_config.agent_performance_tracking_url,  # type: ignore
        stytch_project_id=sdk_config.stytch_project_id,  # type: ignore
        stytch_client_id=sdk_config.stytch_client_id,  # type: ignore
        stytch_client_secret=sdk_config.stytch_client_secret,  # type: ignore
    )
default_agent_runs_repository = AgentRunsRepository(client)
default_eva_records_repository = EVARecordsRepository(client)
default_cam_records_repository = CAMRecordsRepository(client)
default_paula_records_repository = PAULARecordsRepository(client)
