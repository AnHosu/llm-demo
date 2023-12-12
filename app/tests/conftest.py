from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Generator

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from app.main import lifespan, start_application


@asynccontextmanager
async def mock_lifespan(app: FastAPI) -> AsyncGenerator:
    """
    Manages the lifespan of mocks.
    """
    yield


@pytest.fixture(scope="session")
def app_mock() -> Generator[FastAPI, Any, None]:
    """
    Starts a mocked version of the API with a lifespan that handles mocks.
    """
    _app = start_application(lifespan=mock_lifespan)
    yield _app


@pytest.fixture(scope="session")
def client_mock(app_mock: FastAPI) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient with overrides fixtures.
    """
    with TestClient(app_mock) as client:
        yield client


@pytest.fixture(scope="session")
def app_test() -> Generator[FastAPI, Any, None]:
    """
    Starts a version of the API with a lifespan that integrates the staging
    databases.
    """
    _app = start_application(lifespan=lifespan)
    yield _app
