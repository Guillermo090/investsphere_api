from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .services import UserService
from typing import List
from .schemas import UserSchema

user_router = APIRouter()

@user_router.get(
    path="/users", 
    tags=["Users"], 
    summary="Get all users",
    description="This endpoint retrieves a list of all registered users.",
    status_code=status.HTTP_200_OK,
    response_model=List[UserSchema],
    responses={
        status.HTTP_200_OK: {
            "description": "Successful response",
            "content": {"application/json": {"example": [
                {"id":1,"username":"John Doe"},
                {"id":2,"username": "Jane Smith"}
            ]}},
        },
    }
)
def get_users():
    user_service = UserService()
    all_users: List[dict] = user_service.get_all_users()
    all_users = [UserSchema(**user).model_dump() for user in all_users]
    return JSONResponse(status_code=status.HTTP_200_OK, content= all_users )
