from fastapi import FastAPI

from api import router
from core.config import config


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def create_app() -> FastAPI:
    app_ = FastAPI(
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc"
    )

    print(f"\n💌💌💌FastAPI Config is '{config.ENV}'")

    init_routers(app_)

    return app_


app = create_app()
