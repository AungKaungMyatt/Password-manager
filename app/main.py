from litestar import Litestar

from app.api.auth import register
from app.db.dependencies import provide_db_session

app = Litestar(
    route_handlers=[
        register,
    ],
    dependencies={
        "db_session": provide_db_session
    }
)