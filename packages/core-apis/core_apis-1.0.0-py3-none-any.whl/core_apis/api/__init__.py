# -*- coding: utf-8 -*-

"""
FastAPI application factory and configuration.

This module provides the main application factory function for creating
configured FastAPI instances with routing, middleware, and health checks.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import routers
from .routers.health import health_router


def create_application(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    name: str = "API Service",
    description: str = "API Service example...",
    version: str = "0.0.1",
    base_path: str = "/api",
    add_cors_middleware: bool = False,
    debug: bool = False,
    **kwargs,
) -> FastAPI:
    """
    It creates the FastAPI application. Remember to inject the routers before
    creating the application like:

    .. code-block:: python

        from fastapi import APIRouter

        from core_apis.api import server
        from core_apis.api.routers import add_router

        router = APIRouter()
        add_router(router)

        @router.get(path="/server_status")
        def new_router():
            return {"status": "OK"}

        server.run()
    ..

    :param name: Application name.
    :param description: API description.
    :param version: The version.
    :param base_path: The base path to use when the routes are registered.
    :param add_cors_middleware: True to add CORS middleware.
    :param debug: True for debugging.
    :param kwargs: Other arguments.

    :return: Returns the FastAPI application.
    """

    application = FastAPI(
        title=name, description=description, version=version,
        debug=debug, **kwargs)

    if add_cors_middleware:
        application.add_middleware(
            CORSMiddleware,  # type: ignore
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"]
        )

    # By default, the health router is registered...
    routers.append(health_router)

    for router in routers:
        application.include_router(router=router, prefix=base_path)

    return application
