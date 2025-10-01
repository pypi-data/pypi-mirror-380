# -*- coding: utf-8 -*-

"""
CLI runner for API server operations.

This module provides Click-based command-line interface commands for running
and managing the API server. It allows running the server with either a default
or custom FastAPI application instance.
"""

from contextlib import suppress

from click.decorators import group


@group()
def cli_api():
    """
    Click command group for API-related operations.

    This group serves as the parent for all API management commands.
    A custom FastAPI application can be attached via the 'app' attribute
    to override the default application creation.
    """


@cli_api.command("run-api")
def run_api():
    """
    Start the API server.

    This command launches the API server using uvicorn. If a custom FastAPI
    application has been attached to the cli_api group via the 'app' attribute,
    it will be used. Otherwise, a default application will be created.

    The server configuration (host, port, log level) is controlled via
    environment variables in the server.run() function.
    """

    from core_apis.api import server  # pylint: disable=import-outside-toplevel

    app = None
    with suppress(AttributeError):
        app = cli_api.app  # type: ignore

    server.run(app)
