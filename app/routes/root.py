from fastapi import APIRouter


router = APIRouter(
    prefix="/library",
    responses={404: {"description": "Not found"}},
    tags=["library"],
)


@router.get("/ping/")
def ping():
    """Heartbeat endpoint"""
    return "."
