from fastapi import APIRouter

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
