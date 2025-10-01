from __future__ import annotations

from typing import Any, Dict, Optional
import asyncio

import httpx

from .exceptions import APIError, APIResponseError
from .models import PayInRequestSchema


class ThreeXPayClient:
    """Asynchronous client for 3X PAY API."""

    def __init__(
        self,
        api_key: str,
        *,
        is_test: Optional[bool] = None,
        merchant_callback_url: Optional[str] = None,
        merchant_return_url: Optional[str] = None,
        base_url: str = "https://app.3xpay.org",
        timeout: float = 10.0,
        client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        self._api_key = api_key
        self._is_test = is_test
        self._merchant_callback_url = merchant_callback_url
        self._merchant_return_url = merchant_return_url

        self._base_url = base_url.rstrip("/")
        self._owns_client = client is None
        self._client = client or httpx.AsyncClient(base_url=self._base_url, timeout=timeout)

    async def aclose(self) -> None:
        if self._owns_client:
            await self._client.aclose()

    async def __aenter__(self) -> "ThreeXPayClient":  # noqa: D401
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:  # noqa: D401
        await self.aclose()

    def __del__(self) -> None:  # best-effort cleanup
        try:
            if not self._owns_client:
                return
            client = getattr(self, "_client", None)
            if client is None:
                return
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                # No running loop: create a temporary one
                try:
                    asyncio.run(client.aclose())
                except Exception:
                    pass
            else:
                # Running loop: schedule background close
                try:
                    loop.create_task(client.aclose())
                except Exception:
                    pass
        except Exception:
            # Never raise from __del__
            pass

    # --- Public API methods ---
    async def ping(self) -> Dict[str, Any]:
        """Ping health endpoint."""
        response = await self._client.get("/api/ping")
        self._raise_for_status(response)
        payload = response.json()
        self._raise_for_success_false(response, payload)
        return payload

    async def create_payin(
        self,
        amount: float,
        currency: str,
        merchant_order_id: str,
        is_test: Optional[bool] = None,
        merchant_callback_url: Optional[str] = None,
        merchant_return_url: Optional[str] = None,
    ) -> PayInRequestSchema:
        """Create a payin request.

        POST /api/merchant/v1/payin
        """
        payload = {
            "amount": amount,
            "currency": currency,
            "merchant_order_id": merchant_order_id,
            "merchant_callback_url": merchant_callback_url or self._merchant_callback_url,
            "merchant_return_url": merchant_return_url or self._merchant_return_url,
            "is_test": is_test or self._is_test,
        }

        response = await self._client.post(
            "/api/merchant/v1/payin",
            headers=self._auth_headers(),
            json=payload,
        )
        self._raise_for_status(response)
        payload_json = response.json()
        self._raise_for_success_false(response, payload_json)
        return PayInRequestSchema.model_validate(payload_json['data'])

    async def get_payin(self, payin_id: int) -> PayInRequestSchema:
        """Get a payin by id.

        GET /api/merchant/v1/payin?payin_id=...
        """
        response = await self._client.get(
            "/api/merchant/v1/payin", headers=self._auth_headers(), params={"payin_id": payin_id}
        )
        self._raise_for_status(response)
        payload = response.json()
        self._raise_for_success_false(response, payload)
        return PayInRequestSchema.model_validate(payload['data'])

    # --- Internal helpers ---
    def _auth_headers(self) -> Dict[str, str]:
        return {"Api-Key": self._api_key}

    @staticmethod
    def _raise_for_status(response: httpx.Response) -> None:
        if response.is_success:
            return
        try:
            payload = response.json()
            message = payload.get("detail") or payload.get("message")
        except Exception:
            message = None
        raise APIError(response.status_code, message=message, response_text=response.text)

    @staticmethod
    def _raise_for_success_false(response: httpx.Response, payload: Dict[str, Any]) -> None:
        if isinstance(payload, dict) and payload.get("success") is False:
            raise APIResponseError(
                code=payload.get("code"),
                detail=payload.get("detail"),
                traceback_id=payload.get("traceback"),
                status_code=response.status_code,
                response_text=response.text,
            )


