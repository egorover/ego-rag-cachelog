import os
from typing import Optional

DEFAULT_OPENAI_BASE_URL = "https://api.openai.com/v1"
PROXYAPI_BASE_URL = "https://api.proxyapi.ru/openai/v1"


def get_openai_client_kwargs(api_key: Optional[str] = None) -> dict:
    """
    Возвращает параметры для инициализации клиента OpenAI.

    Поддерживаются два режима:
    1. Обычное подключение к OpenAI (по умолчанию)
    2. Подключение через ProxyAPI
    """
    provider = (os.getenv("OPENAI_PROVIDER") or "openai").strip().lower()
    resolved_api_key = api_key or os.getenv("OPENAI_API_KEY")

    kwargs = {
        "api_key": resolved_api_key,
    }

    base_url = os.getenv("OPENAI_BASE_URL")
    if not base_url:
        if provider == "proxyapi":
            base_url = PROXYAPI_BASE_URL
        else:
            base_url = DEFAULT_OPENAI_BASE_URL

    if base_url:
        kwargs["base_url"] = base_url

    return {
        "client_kwargs": kwargs,
        "provider": provider,
        "base_url": base_url,
    }
