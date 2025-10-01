from __future__ import annotations

from typing import Optional

from ._base_client import BaseClient
from .resources.messages import Messages
from .resources.models import Models
from .resources.integrations import Integrations


class Incredible(BaseClient):
    """Anthropic-compatible client for the Incredible API."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float | None = None,
        max_retries: int = BaseClient.DEFAULT_MAX_RETRIES,
        default_headers: Optional[dict[str, str]] = None,
        default_query: Optional[dict[str, object]] = None,
        http_client=None,
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout or BaseClient.DEFAULT_TIMEOUT,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
        )

        self.messages = Messages(self)
        self.models = Models(self)
        self.integrations = Integrations(self)

    def with_options(
        self,
        *,
        timeout: Optional[float] = None,
        default_headers: Optional[dict[str, str]] = None,
        default_query: Optional[dict[str, object]] = None,
    ) -> "Incredible":
        client = super().with_options(
            timeout=timeout,
            default_headers=default_headers,
            default_query=default_query,
        )
        client.messages = Messages(client)
        client.models = Models(client)
        client.integrations = Integrations(client)
        return client

