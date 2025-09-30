from datetime import datetime
from typing import Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from t_reporting_sdk.domain.agent_runs.models import AgentRun
from t_reporting_sdk.repositories.api_clients.agent_performance_tracking.stytch_auth import (
    StytchAuth,
)


class AgentPerformanceTrackingClient:
    def __init__(
        self,
        url: str,
        stytch_project_id: str,
        stytch_client_id: str,
        stytch_client_secret: str,
    ):
        self._base_url = url
        self._session = requests.Session()
        self._session.auth = StytchAuth(
            project_id=stytch_project_id,
            client_id=stytch_client_id,
            client_secret=stytch_client_secret,
        )

        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=[
                "HEAD",
                "GET",
                "OPTIONS",
                "POST",
                "PUT",
                "PATCH",
                "DELETE",
            ],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self._session.mount("https://", adapter)

    def create_agent_run(
        self, run_id: int, run_date: Optional[datetime] = None
    ) -> AgentRun:
        payload = {"run_id": run_id, "run_date": run_date}
        response = self._session.post(
            url=f"{self._base_url}/agent-runs",
            json=payload,
        )
        response.raise_for_status()
        if response.status_code != 201:
            raise RuntimeError("Failed to create agent run.")

        return AgentRun.model_validate(response.json())

    def create_eva_record(
        self,
        agent_run_id: str,
        status: str,
        exception_type: Optional[str],
        message: str,
        customer_id: str,
        patient_id: str,
        payer_id: Optional[str],
        payer_name: Optional[str],
        portal: str,
        insurance_eligibility: Optional[str],
        insurance_type: Optional[str],
    ) -> None:
        json_body = {
            "agent_run_id": agent_run_id,
            "status": status,
            "exception_type": exception_type,
            "message": message,
            "customer_id": customer_id,
            "patient_id": patient_id,
            "payer_id": payer_id,
            "payer_name": payer_name,
            "portal": portal,
            "description": "placeholder",  # TODO: remove this once no longer required on the backend
            "insurance_eligibility": insurance_eligibility,
            "insurance_type": insurance_type,
        }
        response = self._session.post(
            url=f"{self._base_url}/records/eva",
            json=json_body,
        )
        response.raise_for_status()
        if response.status_code != 202:
            raise RuntimeError("Failed to create EVA record.")

    def create_cam_record(
        self,
        agent_run_id: str,
        status: str,
        exception_type: Optional[str],
        message: Optional[str],
        customer_id: str,
        claim_id: str,
        work: str,
        actioned: bool,
    ) -> None:
        json_body = {
            "agent_run_id": agent_run_id,
            "status": status,
            "exception_type": exception_type,
            "message": message,
            "customer_id": customer_id,
            "claim_id": claim_id,
            "work": work,
            "actioned": actioned,
        }
        response = self._session.post(
            url=f"{self._base_url}/records/cam",
            json=json_body,
        )
        response.raise_for_status()
        if response.status_code != 202:
            raise RuntimeError("Failed to create CAM record.")

    def create_paula_record(
        self,
        agent_run_id: str,
        status: str,
        exception_type: Optional[str],
        message: Optional[str],
        customer_id: str,
        original_status: str,
        patient_id: str,
        portal: str,
        appointment_date: str,
        treatment_code: str,
        payer: Optional[str],
        payer_id: Optional[str],
        plan_id: Optional[str],
        system_of_record_id: str,
        authorization_id: Optional[str],
    ) -> None:
        json_body = {
            "agent_run_id": agent_run_id,
            "status": status,
            "exception_type": exception_type,
            "message": message,
            "customer_id": customer_id,
            "original_status": original_status,
            "patient_id": patient_id,
            "portal": portal,
            "appointment_date": appointment_date,
            "treatment_code": treatment_code,
            "payer": payer,
            "payer_id": payer_id,
            "plan_id": plan_id,
            "system_of_record_id": system_of_record_id,
            "authorization_id": authorization_id,
        }
        response = self._session.post(
            url=f"{self._base_url}/records/paula",
            json=json_body,
        )
        response.raise_for_status()
        if response.status_code != 202:
            raise RuntimeError("Failed to create PAULA record.")
