import os

from fastapi import APIRouter, UploadFile

from app.core.bedrock import BedrockService
from app.core.prompts import prompt_complaint, prompt_complaints


bedrock_client = BedrockService(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region=os.getenv("AWS_REGION")
)

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"],
    responses={404: {"description": "Not found"}}
)


@router.get("/prompt", response_model=dict)
def prompt(prompt: str) -> dict:
    """
    Prompt the model and get a reply.
    """
    return {"reply": bedrock_client.prompt(prompt=prompt)}


@router.get("/parse_one", response_model=dict)
def summarise_complaint(prompt: str) -> dict:
    """
    Prompt the model to summarise a customer complaint.
    """
    modified_prompt = prompt_complaint(prompt=prompt)
    return {"reply": bedrock_client.prompt(prompt=modified_prompt)}


@router.post("/parse_more")
async def summarise_complaints(prompt: str, file: UploadFile) -> dict:
    """
    Prompt the model to summarise multiple customer complaints in an uploaded
    text file.
    """
    contents = await file.read()
    modified_prompt = prompt_complaints(
        prompt=contents,
        additional_prompt=prompt
    )
    return {"reply": bedrock_client.prompt(prompt=modified_prompt)}
