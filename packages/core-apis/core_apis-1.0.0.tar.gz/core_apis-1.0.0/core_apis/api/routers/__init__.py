# -*- coding: utf-8 -*-

"""
Router management for FastAPI applications.

This module provides a registry for dynamically adding routers to the
FastAPI application before it's created.
"""

from typing import List

from fastapi import APIRouter


# Inject the routers...
routers: List[APIRouter] = []


def add_router(router: APIRouter) -> None:
    """
    Register a router to be included in the FastAPI application.

    Routers must be added before calling create_application() to be
    included in the final application instance.

    Args:
        router: The APIRouter instance to register.
    """
    routers.append(router)
