import os
import pytest

from t_reporting_sdk.config import Backend, ReportingSDKConfig


class TestReportingSDKConfig:
    def setup_class(self):
        os.environ["FABRIC_BASE_URL"] = "http://localhost:8000"
        os.environ["FABRIC_USER_EMAIL"] = "default@reporter.test"
        os.environ["FABRIC_USER_OTP_SECRET"] = "fake_secret"
        os.environ["AGENT_PERFORMANCE_TRACKING_URL"] = "http://localhost:9000"
        os.environ["STYTCH_PROJECT_ID"] = "test_project_id"
        os.environ["STYTCH_CLIENT_ID"] = "test_client_id"
        os.environ["STYTCH_CLIENT_SECRET"] = "test_client_secret"

    def teardown_class(self):
        del os.environ["FABRIC_BASE_URL"]
        del os.environ["FABRIC_USER_EMAIL"]
        del os.environ["FABRIC_USER_OTP_SECRET"]
        del os.environ["AGENT_PERFORMANCE_TRACKING_URL"]
        del os.environ["STYTCH_PROJECT_ID"]
        del os.environ["STYTCH_CLIENT_ID"]
        del os.environ["STYTCH_CLIENT_SECRET"]

    @pytest.mark.unit
    def test_singleton(self):
        config1 = ReportingSDKConfig()
        config2 = ReportingSDKConfig()
        config3 = ReportingSDKConfig.configure()

        assert config1 is config2
        assert config1 is config3

    @pytest.mark.unit
    def test_default_values(self):
        config = ReportingSDKConfig()

        assert config.backend == Backend.FABRIC
        assert config.fabric_client_config.base_url == "http://localhost:8000"
        assert config.fabric_client_config.user_email == "default@reporter.test"
        assert config.fabric_client_config.user_otp_secret == "fake_secret"

    @pytest.mark.unit
    def test_partial_configure(self):
        ReportingSDKConfig.configure(fabric_base_url="http://localhost:8001")

        config = ReportingSDKConfig()

        assert config.fabric_client_config.base_url == "http://localhost:8001"
        assert config.fabric_client_config.user_email == "default@reporter.test"
        assert config.fabric_client_config.user_otp_secret == "fake_secret"

    @pytest.mark.unit
    def test_configure(self):
        ReportingSDKConfig.configure(
            fabric_base_url="http://localhost:8001",
            fabric_user_email="non_default@reporter.test",
            fabric_user_secret="another_fake_secret",
        )

        config = ReportingSDKConfig()

        assert config.fabric_client_config.base_url == "http://localhost:8001"
        assert config.fabric_client_config.user_email == "non_default@reporter.test"
        assert config.fabric_client_config.user_otp_secret == "another_fake_secret"

    @pytest.mark.unit
    def test_configure_thoughthub(self):
        ReportingSDKConfig.configure(
            backend=Backend.THOUGHTHUB,
            agent_performance_tracking_url="http://localhost:9001",
            stytch_project_id="another_test_project_id",
            stytch_client_id="another_test_client_id",
            stytch_client_secret="another_test_client_secret",
        )

        config = ReportingSDKConfig()

        assert config.backend == Backend.THOUGHTHUB
        assert config.agent_performance_tracking_url == "http://localhost:9001"
        assert config.stytch_project_id == "another_test_project_id"
        assert config.stytch_client_id == "another_test_client_id"
        assert config.stytch_client_secret == "another_test_client_secret"
