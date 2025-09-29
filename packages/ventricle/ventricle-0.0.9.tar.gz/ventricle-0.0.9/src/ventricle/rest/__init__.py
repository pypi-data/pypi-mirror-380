from fastapi import FastAPI
from ._ping import ping_router


def create_rest_app() -> FastAPI:
    """
    Create and configure a FastAPI REST application.
    :return: The configured FastAPI REST application.
    """
    app = FastAPI(title="Ventricle")

    app.include_router(ping_router)

    return app