# -*- coding: utf-8 -*-

"""
Health check router for API monitoring.

This module provides a simple health check endpoint that can be used
for monitoring, load balancer health checks, and service discovery.
"""

from fastapi import APIRouter
from starlette.responses import PlainTextResponse
from starlette.status import HTTP_200_OK


health_router = APIRouter()


@health_router.get(
    path="/ping",
    status_code=HTTP_200_OK,
    response_class=PlainTextResponse,
    description="Endpoint to ensure the API service is listening...")
def health():
    """
    It's the default endpoint is injected to the API...
    [GET] /api/ping -> return "PONG"
    """

    return "PONG"
