import os

from fastapi import APIRouter

from app.core.bedrock import BedrockService


bedrock_client = BedrockService(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region=os.getenv("AWS_REGION")
)

router = APIRouter(
    prefix="",
    tags=["Root"],
    responses={404: {"description": "Not found"}}
)


@router.get("/health_check", response_model=dict)
async def health_check():
    """
    API hearbeat / health check.
    """
    return {"msg": "healthy"}


@router.get("/prompt", response_model=dict)
async def prompt(prompt: str) -> dict:
    """
    Prompt the model and get a reply.
    """
    return {"reply": bedrock_client.prompt(prompt=prompt)}
