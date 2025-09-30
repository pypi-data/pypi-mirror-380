"""Viewer module for doweb."""

from collections.abc import Iterable
from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.routing import WebSocketRoute

from . import config
from .api.viewer import router

# from .layout_server import EditableLayoutViewServerEndpoint
from .layout_server import LayoutViewServerEndpoint


def get_app(
    fileslocation: Path | str,
    *,
    editable: bool = True,
    allowed_modes: Iterable[str] = (
        "select",
        "move instances",
        "ruler",
        "cross",
        "box ruler",
    ),
) -> FastAPI:
    """Create and configure the viewer FastAPI application."""
    # config.settings.fileslocation = Path(fileslocation)
    _settings = config.Config(fileslocation=Path(fileslocation), editable=editable)

    def settings() -> config.Config:
        return _settings

    staticfiles = StaticFiles(directory=Path(__file__).parent / "static")

    class BrowserLayoutViewServerEndpoint(
        LayoutViewServerEndpoint,
        root=_settings.fileslocation,
        editable=editable,
        add_missing_layers=_settings.add_missing_layers,
        meta_splitter=_settings.meta_splitter,
        allowed_modes=list(allowed_modes),
        max_rdb_limit=_settings.max_rdb_limit,
    ):
        pass

    app = FastAPI(
        routes=[WebSocketRoute("/ws", endpoint=BrowserLayoutViewServerEndpoint)]
    )

    # insert the settings as the first dependency
    router.dependencies.insert(0, Depends(settings))
    app.include_router(router)
    app.mount("/static", staticfiles, name="doweb_static")

    return app
