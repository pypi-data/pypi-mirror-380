"""
Cloud Mode implementations using REST API.
"""

from typing import Any, Dict, List, Optional
import httpx

from .base import (
    LabelOperation,
    AIOperation,
    ExtractOperation,
    AnonymizeOperation,
    DescribeOperation
)
from ..models import SingleLabelResult, MultipleLabelResult


class CloudLabelOperation(LabelOperation):
    """Cloud-based labeling implementation using REST API."""
    
    def __init__(self, api_key: str, api_endpoint: str):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self._http_client = None
    
    def _get_http_client(self):
        """Lazy initialization of HTTP client."""
        if self._http_client is None or self._http_client.is_closed:
            self._http_client = httpx.AsyncClient(
                headers={"X-API-KEY": self.api_key}
            )
        return self._http_client
    
    async def label_single(self, text: str, labels: List[str]) -> SingleLabelResult:
        """Cloud implementation of single label classification."""
        async with httpx.AsyncClient(headers={"X-API-KEY": self.api_key}) as client:
            try:
                response = await client.post(
                    f"{self.api_endpoint}/api/v1/label",
                    json={"text": text, "categories": labels, "multiple": False}
                )
                response.raise_for_status()
                data = response.json()
                return SingleLabelResult(**data["result"])
            except Exception as e:
                raise RuntimeError(f"Cloud labeling failed: {str(e)}") from e
    
    async def label_multiple(self, text: str, labels: List[str]) -> MultipleLabelResult:
        """Cloud implementation of multiple label classification."""
        async with httpx.AsyncClient(headers={"X-API-KEY": self.api_key}) as client:
            try:
                response = await client.post(
                    f"{self.api_endpoint}/api/v1/label",
                    json={"text": text, "categories": labels, "multiple": True}
                )
                response.raise_for_status()
                data = response.json()
                return MultipleLabelResult(**data["result"])
            except Exception as e:
                raise RuntimeError(f"Cloud labeling failed: {str(e)}") from e


class CloudAIOperation(AIOperation):
    """Cloud-based AI transformation implementation using REST API."""
    
    def __init__(self, api_key: str, api_endpoint: str):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self._http_client = None
    
    def _get_http_client(self):
        """Lazy initialization of HTTP client."""
        if self._http_client is None or self._http_client.is_closed:
            self._http_client = httpx.AsyncClient(
                headers={"X-API-KEY": self.api_key}
            )
        return self._http_client
    
    async def ai(self, prompt: str, data: str) -> str:
        """Cloud implementation of AI transformation."""
        async with httpx.AsyncClient(headers={"X-API-KEY": self.api_key}) as client:
            try:
                response = await client.post(
                    f"{self.api_endpoint}/api/v1/ai",
                    json={"prompt": prompt, "text": data}
                )
                response.raise_for_status()
                data = response.json()
                return data["result"]
            except httpx.HTTPStatusError as e:
                # Get detailed error response
                try:
                    error_detail = e.response.json()
                    error_msg = f"HTTP {e.response.status_code}: {error_detail}"
                except:
                    error_msg = f"HTTP {e.response.status_code}: {e.response.text}"
                raise RuntimeError(f"Cloud AI transformation failed: {error_msg}") from e
            except Exception as e:
                raise RuntimeError(f"Cloud AI transformation failed: {str(e)}") from e


class CloudExtractOperation(ExtractOperation):
    """Cloud-based extraction implementation using REST API."""
    
    def __init__(self, api_key: str, api_endpoint: str):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self._http_client = None
    
    def _get_http_client(self):
        """Lazy initialization of HTTP client."""
        if self._http_client is None or self._http_client.is_closed:
            self._http_client = httpx.AsyncClient(
                headers={"X-API-KEY": self.api_key}
            )
        return self._http_client
    
    async def extract(self, extraction_type: str, text: str) -> List[str]:
        """Cloud implementation of information extraction."""
        client = self._get_http_client()
        
        try:
            response = await client.post(
                f"{self.api_endpoint}/api/v1/extract",
                json={"field": extraction_type, "text": text}
            )
            response.raise_for_status()
            data = response.json()
            return data["result"]
        except Exception as e:
            raise RuntimeError(f"Cloud information extraction failed: {str(e)}") from e


class CloudAnonymizeOperation(AnonymizeOperation):
    """Cloud-based anonymization implementation using REST API."""
    
    def __init__(self, api_key: str, api_endpoint: str):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self._http_client = None
    
    def _get_http_client(self):
        """Lazy initialization of HTTP client."""
        if self._http_client is None or self._http_client.is_closed:
            self._http_client = httpx.AsyncClient(
                headers={"X-API-KEY": self.api_key}
            )
        return self._http_client
    
    async def anonymize(self, text: str) -> str:
        """Cloud implementation of text anonymization."""
        client = self._get_http_client()
        
        try:
            response = await client.post(
                f"{self.api_endpoint}/api/v1/anonymize",
                json={"text": text}
            )
            response.raise_for_status()
            data = response.json()
            return data["result"]
        except Exception as e:
            raise RuntimeError(f"Cloud anonymization failed: {str(e)}") from e


class CloudDescribeOperation(DescribeOperation):
    """Cloud-based description generation implementation using REST API."""
    
    def __init__(self, api_key: str, api_endpoint: str):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self._http_client = None
    
    def _get_http_client(self):
        """Lazy initialization of HTTP client."""
        if self._http_client is None or self._http_client.is_closed:
            self._http_client = httpx.AsyncClient(
                headers={"X-API-KEY": self.api_key}
            )
        return self._http_client
    
    async def describe(self, features: Dict[str, Any], style: str) -> str:
        """Cloud implementation of feature description generation."""
        client = self._get_http_client()
        
        try:
            response = await client.post(
                f"{self.api_endpoint}/api/v1/describe",
                json={"features": features, "style": style}
            )
            response.raise_for_status()
            data = response.json()
            return data["result"]
        except Exception as e:
            raise RuntimeError(f"Cloud description generation failed: {str(e)}") from e
