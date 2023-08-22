from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}
