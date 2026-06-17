from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import os
from pathlib import Path


def _load_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def _get_value(key: str, default: str, env_file_values: dict[str, str]) -> str:
    return os.environ.get(key, env_file_values.get(key, default))


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_version: str
    service_name: str
    environment: str
    database_url: str


def load_settings(env_file: str | Path = ".env") -> Settings:
    env_file_values = _load_env_file(Path(env_file))
    return Settings(
        app_name=_get_value("EXECUBOT_APP_NAME", "ExecuBot Kernel", env_file_values),
        app_version=_get_value("EXECUBOT_APP_VERSION", "0.1.0", env_file_values),
        service_name=_get_value("EXECUBOT_SERVICE_NAME", "execubot-api", env_file_values),
        environment=_get_value("EXECUBOT_ENV", "development", env_file_values),
        database_url=_get_value(
            "DATABASE_URL",
            "postgresql+psycopg://execubot:execubot_dev_password@localhost:5432/execubot",
            env_file_values,
        ),
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return load_settings()
