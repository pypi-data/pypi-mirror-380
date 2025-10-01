from __future__ import annotations

import json
import time
import logging
from functools import wraps
from typing import Dict, Optional, Union, Any
from urllib.parse import urljoin

import requests

from . import __version__
from .exceptions import ValidationError, LicenseError, APIError
from .models import Config, AccessResult

logger = logging.getLogger(__name__)

def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, APIError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
                        logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
            # si agotó los reintentos, propaga el último error
            raise last_exception
        return wrapper
    return decorator


class AccessSDK:
    # Asegúrate que BASE_URL termina con / y que ENDPOINT es correcto en tu backend
    BASE_URL = "https://dsf-access-2ukruhvbi-jaime-alexander-jimenezs-projects.vercel.app/"
    ENDPOINT = "api/evaluate"  # <— ajusta si tu server usa otra ruta, p.ej. "" o "evaluate"
    TIERS = {"community", "professional", "enterprise"}

    def __init__(
        self,
        license_key: Optional[str] = None,
        tier: str = "community",
        base_url: Optional[str] = None,
        timeout: int = 30,
        verify_ssl: bool = True,
    ):
        if tier not in self.TIERS:
            raise ValidationError(f"Invalid tier: {self.TIERS}")

        self.license_key = license_key
        self.tier = tier
        self.base_url = base_url or self.BASE_URL
        self.timeout = timeout
        self.verify_ssl = verify_ssl

        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": f"DSF-Access-SDK-Python/{__version__}",
        })

        if tier != "community" and license_key:
            self._validate_license()

    def _endpoint(self) -> str:
        # Permite cambiar ENDPOINT a "" si tu API espera en la raíz
        return self.ENDPOINT

    def _validate_license(self):
        try:
            response = self._make_request(self._endpoint(), {
                "data": {},
                "config": {"test": {"default": 1, "weight": 1.0}},
                "tier": self.tier,
                "license_key": self.license_key,
            })
            if not response.get("tier"):
                raise LicenseError("License validation failed")
        except APIError as e:
            if e.status_code == 403:
                raise LicenseError(f"Invalid license: {e.message}")
            raise

    @retry_on_failure(max_retries=3)
    def _make_request(self, endpoint: str, data: Dict) -> Dict:
        url = urljoin(self.base_url, endpoint)
        try:
            resp = self.session.post(url, json=data, timeout=self.timeout, verify=self.verify_ssl)
            if resp.status_code == 200:
                try:
                    return resp.json()
                except json.JSONDecodeError:
                    raise APIError("Invalid JSON response from server", status_code=200)

            # intenta extraer mensaje de error
            try:
                err = resp.json()
            except Exception:
                err = {"error": (resp.text or "API error").strip()}

            if resp.status_code == 403:
                raise LicenseError(err.get("error", "License error"))
            raise APIError(err.get("error", "API error"), status_code=resp.status_code)
        except requests.RequestException as e:
            raise APIError(f"Request failed: {e}")

    def evaluate(self, data, config=None, custom_confidence: float | None = None) -> AccessResult:
        if isinstance(config, Config):
            config = config.to_dict()
        if not isinstance(data, dict):
            raise ValidationError("Data must be a dictionary")

        payload = {"data": data, "config": config or {}, "tier": self.tier}
        if self.license_key:
            payload["license_key"] = self.license_key
        if custom_confidence is not None:
            if not 0.0 <= custom_confidence <= 1.0:
                raise ValidationError("Confidence must be between 0.0 and 1.0")
            payload["confidence_level"] = custom_confidence

        response = self._make_request(self._endpoint(), payload)
        return AccessResult.from_response(response)

    def create_config(self) -> Config:
        return Config()

    def get_metrics(self) -> Optional[Dict]:
        if self.tier == "community":
            return None
        response = self._make_request(self._endpoint(), {
            "data": {},
            "config": {},
            "tier": self.tier,
            "license_key": self.license_key,
            "get_metrics": True,
        })
        return response.get("metrics")

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

