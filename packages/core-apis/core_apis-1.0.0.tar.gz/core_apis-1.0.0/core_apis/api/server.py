# -*- coding: utf-8 -*-

"""
API server module for running FastAPI applications.

This module provides functionality to start and run a FastAPI application
using uvicorn as the ASGI server. Configuration is controlled through
environment variables for flexibility in different deployment environments.
"""

import os
import typing

import uvicorn
from fastapi import FastAPI

from core_apis.api import create_application


def run(app: typing.Optional[FastAPI] = None) -> None:
    """
    Start the API server using uvicorn.

    Launches a FastAPI application with uvicorn ASGI server. If no application
    is provided, a default application will be created with CORS middleware enabled.

    Args:
        app: Optional FastAPI application instance. If None, a default application
             will be created using environment configuration.

    Environment Variables:
        API_NAME: Name of the API service (default: "API-Service")
        DEBUG: Enable debug mode, set to "1" to enable (default: disabled)
        HOST: Server host address (default: "127.0.0.1" for security)
        PORT: Server port number (default: 3500)
        LOG_LEVEL: Uvicorn log level (default: "info")

    Note:
        The default host is "127.0.0.1" (localhost only) for security.
        To expose the server to all interfaces, set HOST="0.0.0.0".
    """

    if not app:
        app = create_application(
            name=os.getenv("API_NAME", "API-Service"),
            debug=os.getenv("DEBUG") == "1",
            add_cors_middleware=True,
        )

    # Get port with error handling
    try:
        port = int(os.getenv("PORT", "3500"))
    except ValueError:
        port = 3500

    uvicorn.run(
        app=app,
        host=os.getenv("HOST", "127.0.0.1"),
        port=port,
        log_level=os.getenv("LOG_LEVEL", "info"),
    )
