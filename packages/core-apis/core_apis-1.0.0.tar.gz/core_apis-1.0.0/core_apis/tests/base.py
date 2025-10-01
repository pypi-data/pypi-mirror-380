# -*- coding: utf-8 -*-

"""
Base test classes for API testing.

This module provides base test case classes that can be inherited by other test modules
to facilitate testing of FastAPI applications. It includes utilities for setting up
test clients and managing test application instances.
"""

from typing import Optional
from unittest import TestCase

from fastapi import FastAPI
from starlette.testclient import TestClient

from core_apis.api import create_application


class BaseApiTestCases(TestCase):
    """
    Base class for tests related to the API.

    This class provides a reusable foundation for API testing by automatically
    setting up a FastAPI test application and test client. Tests that inherit
    from this class will have access to a configured TestClient instance.

    Attributes:
        client: The Starlette TestClient instance for making test requests.
        app: The FastAPI application instance being tested.
    """

    client: Optional[TestClient] = None
    app: Optional[FastAPI] = None

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the test class before any test methods run.

        This method is called once per test class and initializes the
        test client and application instance.
        """

        super().setUpClass()
        cls.init_client()

    @classmethod
    def init_client(cls, with_cors: bool = True):
        """
        Initialize the test client and FastAPI application.

        Creates a new FastAPI application instance configured for testing
        and wraps it with a TestClient for making HTTP requests.

        Args:
            with_cors: Whether to add CORS middleware to the test application.
                       Defaults to True.
        """

        app = create_application(
            name="API-Tests",
            add_cors_middleware=with_cors,
        )

        cls.client = TestClient(app)
        cls.app = app
