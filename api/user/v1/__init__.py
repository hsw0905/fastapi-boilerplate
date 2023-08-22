from fastapi import APIRouter

from .controller import user_router

sub_router = APIRouter()
sub_router.include_router(user_router, prefix="/api/v1/users", tags=["User"])
