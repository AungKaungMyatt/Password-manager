# this creates an asynchronous SQLAlchemy engine and 
# session maker for database interactions in the application. 
# The `AsyncSessionLocal` can be used to create new sessions for database operations, 
# and the `engine` is configured to connect to the database specified 
# in the application's settings.

from sqlalchemy.ext.asyncio import (
    AsyncSession, 
    async_sessionmaker, 
    create_async_engine,
)

from app.core.config import settings

engine = create_async_engine(settings.database_url, echo=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)