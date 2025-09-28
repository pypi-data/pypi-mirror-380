# -*- coding: utf-8 -*-

"""
Base test utilities for Sentry SDK integration testing.

This module provides a common base class that automatically mocks sentry_sdk.init
for all Sentry-related test cases, ensuring tests run in isolation without making
actual network calls to Sentry.

Classes:
    BaseSentryTestCases: Base test class with automatic Sentry SDK mocking.

Example:
    Create a test class that inherits from BaseSentryTestCases:

    .. code-block:: python

        from core_sentry.tests.base import BaseSentryTestCases

        class MyTests(BaseSentryTestCases):
            def test_sentry_integration(self):
                # sentry_sdk.init is automatically mocked
                # Access the mock via self.sentry_mock
                pass
    ..

Key Components:
  1. Automatic Sentry Mocking:
    - Creates a patcher for sentry_sdk.init
    - Stores the mock object for test assertions

  2. Class-level Setup/Teardown:
    - setUpClass() starts the patcher and stores the mock
    - tearDownClass() stops the patcher

Benefits:
  - Prevents actual Sentry initialization during tests
  - Consistent mocking across all test classes that inherit from it
  - Clean test isolation - each test class gets fresh mocking
  - Reduces boilerplate - no need to manually patch sentry_sdk.init in each test
  - Provides access to the mock object for assertions
"""

from unittest import TestCase
from unittest.mock import patch


class BaseSentryTestCases(TestCase):
    """ Base class for Test Cases related to Sentry integration """

    sentry_patcher = patch(target="sentry_sdk.init")
    sentry_mock = None

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.sentry_mock = cls.sentry_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        cls.sentry_patcher.stop()
