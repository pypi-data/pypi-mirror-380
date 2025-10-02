import requests
from .exceptions import SentorAPIError, RateLimitError, AuthenticationError
from typing import TypedDict, List


class DocumentInput(TypedDict):
    """Represents a document to be predicted with its metadata."""

    doc_id: str
    doc: str
    entities: List[str]


class SentorClient:
    """Client for interacting with the Sentor ML API."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://sentor.app/api",
        timeout: int = 30,
    ):
        """
        Initialize the Sentor client with API credentials and configuration.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }

    def predict(self, documents: List[DocumentInput], language: str = "en"):
        """Predict sentiment and entity extraction for documents.

        Args:
            documents: List of documents to predict
            language: Language code for prediction (default: "en").
                Supported languages: "en", "nl"

        Returns:
            dict: Prediction results

        Raises:
            ValueError: If input is empty or invalid language is provided
            RateLimitError: If API rate limit is exceeded
            AuthenticationError: If API key is invalid
            SentorAPIError: For other API errors
        """
        if not documents:
            raise ValueError("Input is required")

        if language not in ["en", "nl"]:
            raise ValueError("Language must be 'en' or 'nl'")

        url = f"{self.base_url}/predicts"
        params = {"language": language}
        payload = {"docs": documents}
        response = requests.post(
            url,
            json=payload,
            headers=self.headers,
            timeout=self.timeout,
            params=params,
        )

        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        elif response.status_code == 429:
            raise RateLimitError(response.json())
        elif response.status_code == 401:
            raise AuthenticationError(response.json())
        else:
            raise SentorAPIError(response.json())

    def check_health(self):
        """Check the health status of the Sentor API.

        Returns:
            dict: Health status information

        Raises:
            SentorAPIError: If health check fails
        """
        url = f"{self.base_url}/predicts/health"
        response = requests.get(
            url,
            headers=self.headers,
            timeout=self.timeout,
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise SentorAPIError(response.json())
