from fastapi import FastAPI

from execubot.api.routes import audit, memory, tasks
from execubot.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version=settings.app_version)
    app.include_router(audit.router)
    app.include_router(memory.router)
    app.include_router(tasks.router)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "service": settings.service_name,
            "environment": settings.environment,
        }

    return app


app = create_app()
