# -*- coding: utf-8 -*-

"""
Sentry SDK initialization decorators.

This module provides decorators for initializing the Sentry SDK with automatic
error tracking and monitoring capabilities. The decorators handle Sentry
initialization, tag setting, and graceful error handling.

Functions:
    init_sentry: Decorator that initializes Sentry SDK and sets tags for a function.

Example:
    Basic usage with required parameters:

    .. code-block:: python

        from core_sentry.decorators.base import init_sentry

        @init_sentry(dsn="https://your-dsn@sentry.io/project", env="production")
        def my_function():
            return "Hello World"
    ..

    Advanced usage with tags and custom configuration:

    .. code-block:: python

        @init_sentry(
            dsn="https://your-dsn@sentry.io/project",
            env="production",
            tags={"service": "api", "version": "1.0"},
            traces_sample_rate=0.1,
            send_default_pii=False
        )
        def api_handler():
            # Function code here
            pass
    ..

Features:
  - Automatic Sentry SDK initialization with provided configuration
  - Tag management for enhanced error tracking and filtering
  - Graceful handling of initialization failures with logging
  - Prevention of duplicate initialization when Sentry is already configured
  - Support for all standard Sentry SDK configuration options
"""

import functools
import logging
import typing

import sentry_sdk


def init_sentry(
    _func: typing.Optional[typing.Callable] = None,
    *,
    dsn: str,
    env: str,
    tags: typing.Optional[typing.Dict] = None,
    traces_sample_rate: float = 0.1,
    **init_args,
) -> typing.Union[typing.Callable, typing.Callable[[typing.Callable], typing.Callable]]:
    """
    It initializes the Sentry's SDK and optionally integrations...

    .. code-block:: python

        @init_sentry(dsn="SomeDSN", env="Env", tags={"project": "SomeProject"}, send_default_pii=False)
        def custom_function(value: int = 0):
            return value
    ..

    :param _func:
    :param dsn: The DSN tells the SDK where to send the events.
    :param env: Environments tell you where an error occurred (production, staging).

    :param tags:
        Tags are key/value string pairs that are both indexed and searchable. Tags power
        features in sentry.io such as filters and tag-distribution maps. Tags also help you quickly
        both access related events and view the tag distribution for a set of events.
        More Info: https://docs.sentry.io/platforms/python/enriching-events/tags/

    :param traces_sample_rate: Controls the percentage of transactions to trace (0.0 to 1.0).
        Defaults to 0.1 (10%) for better performance in production.

    For other parameters: https://docs.sentry.io/platforms/python/configuration/options/
    """

    if tags is None:
        tags = {}

    def set_tags():
        for tag, value in tags.items():
            sentry_sdk.set_tag(key=tag, value=value)

    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Only initialize Sentry if not already initialized...
            if not sentry_sdk.get_client().dsn:
                try:
                    sentry_sdk.init(
                        dsn=dsn,
                        environment=env,
                        traces_sample_rate=traces_sample_rate,
                        **init_args,
                    )

                except Exception as e:
                    logging.warning(f"Failed to initialize Sentry: {e}")

            set_tags()
            return func(*args, **kwargs)

        return wrapper

    if not _func:
        return decorator

    return decorator(_func)
