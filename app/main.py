from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from .v1.endpoints import root


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """
    This function manages the lifespan of resources.
    """
    yield


def start_application(lifespan: AsyncGenerator = None) -> FastAPI:
    """
    Creates a FastAPI instance and attaches all endpoints.
    """
    app = FastAPI(title="My API", lifespan=lifespan)
    app.include_router(root.router)
    return app


# Start API
app = start_application(lifespan=lifespan)
