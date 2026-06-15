from litestar import Litestar

from app.api.auth import register


app = Litestar(
    route_handlers=[
        register,
    ]
)