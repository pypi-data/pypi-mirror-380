import warnings

from galtea.application.services.conversation_simulator_service import ConversationSimulatorService
from galtea.application.services.inference_result_service import InferenceResultService
from galtea.application.services.session_service import SessionService
from galtea.application.services.simulator_service import SimulatorService
from galtea.application.services.test_case_service import TestCaseService

from .application.services.evaluation_service import EvaluationService
from .application.services.metric_service import MetricService
from .application.services.product_service import ProductService
from .application.services.test_service import TestService
from .application.services.version_service import VersionService
from .infrastructure.clients.http_client import Client
from .utils.validate_installed_version import validate_installed_version


class Galtea:
    def __init__(self, api_key: str, suppress_updatable_version_message: bool = False):
        """Initialize the Galtea SDK with the provided API key.
        Args:
            api_key (str): The API key to access the Galtea platform for authentication.
            suppress_updatable_version_message (bool): If True, suppresses the message about a newer version available.
        """
        self.__client = Client(api_key)
        self.products = ProductService(self.__client)
        self.tests = TestService(self.__client, self.products)
        self.test_cases = TestCaseService(self.__client, self.tests)
        self.versions = VersionService(self.__client, self.products)
        self.metrics = MetricService(self.__client)
        self.sessions = SessionService(self.__client)
        self.inference_results = InferenceResultService(self.__client, self.sessions)
        self.evaluations = EvaluationService(self.__client, self.metrics, self.sessions, self.test_cases)
        self.conversation_simulator = ConversationSimulatorService(self.__client)
        self.simulator = SimulatorService(
            self.__client,
            self.sessions,
            self.test_cases,
            self.inference_results,
            self.conversation_simulator,
        )

        # Validate that the installed version of the SDK is compatible with the API
        validate_installed_version(self.__client, suppress_updatable_version_message)

    @property
    def metric_types(self) -> MetricService:
        warnings.warn(
            (
                "galtea.metric_types is deprecated and will be removed in a future release.\n"
                "Use galtea.metrics API instead."
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        return self.metrics

    @metric_types.setter
    def metric_types(self, value: MetricService) -> None:
        warnings.warn(
            (
                "galtea.metric_types is deprecated and will be removed in a future release.\n"
                "Use galtea.metrics API instead."
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        self.metrics = value

    @property
    def evaluation_tasks(self) -> EvaluationService:
        warnings.warn(
            (
                "galtea.evaluation_tasks is deprecated and will be removed in a future release.\n"
                "Use galtea.evaluations API instead."
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        return self.evaluations

    @evaluation_tasks.setter
    def evaluation_tasks(self, value: EvaluationService) -> None:
        warnings.warn(
            (
                "galtea.evaluation_tasks is deprecated and will be removed in a future release.\n"
                "Use galtea.evaluations API instead."
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        self.evaluations = value
