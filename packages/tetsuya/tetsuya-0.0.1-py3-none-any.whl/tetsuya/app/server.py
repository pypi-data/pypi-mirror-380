"""Server implements logic for starting and verifying server."""

from __future__ import annotations

import os
import sys
from http import HTTPStatus
from typing import TYPE_CHECKING

import httpx
import logistro
import uvicorn

from tetsuya._globals import active_services, app, cli, service_types

from .client import get_client
from .utils import uds_path

if TYPE_CHECKING:
    from pathlib import Path


_logger = logistro.getLogger(__name__)


def is_server_alive(uds_path: Path) -> bool:
    """Check if server is running."""
    if not uds_path.exists():
        return False
    client: None | httpx.Client = None
    try:
        client = get_client(uds_path, defer_close=False)
        r = client.get("/ping")
        if r.status_code == HTTPStatus.OK:
            _logger.info("Socket ping returned OK- server alive.")
            return True
        else:
            _logger.info(
                f"Socket ping returned {r.status_code}, removing socket.",
            )
            uds_path.unlink()
            return False
    except httpx.TransportError:
        _logger.info("Transport error in socket, removing socket.")
        uds_path.unlink()
        return False
    finally:
        if client:
            client.close()


@cli.command(name="server")
def start():
    """Start the server."""
    active_services.update(
        {f.__name__: f() for f in service_types},
    )
    if not is_server_alive(p := uds_path()):
        for _s in active_services:
            _logger.info(f"Found: {_s}")
        os.umask(0o077)
        _logger.info("Starting server.")
        uvicorn.run(app, uds=str(p))
    else:
        print("Server already running.", file=sys.stderr)  # noqa: T201
        sys.exit(1)


@app.get("/ping")
def ping():
    """Ping!"""  #  noqa: D400
    _logger.info("Pong!")
    return "pong"
