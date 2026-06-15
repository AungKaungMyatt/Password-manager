from litestar import post
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import (
    UserRegister,
    UserResponse,
)
from app.services.user_service import (
    get_user_by_email,
    create_user,
)

@post("/register")
async def register(
    data: UserRegister,
    db: AsyncSession,
) -> UserResponse:
    existing_user = await get_user_by_email(
        db,
        data.email,
    )

    if existing_user:
        raise ValueError(
            "Email already registered"
        )

    user = await create_user(
        db,
        email=data.email,
        password=data.password,
    )

    return UserResponse(
        id=user.id,
        email=user.email,
    )