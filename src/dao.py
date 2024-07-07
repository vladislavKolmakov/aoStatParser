from sqlalchemy import delete, insert, select
from sqlalchemy.exc import SQLAlchemyError

from src.database import async_session_maker
from src.models import Event, Player


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none() is not None

class EventDAO(BaseDAO):
    model = Event


class PlayerDAO(BaseDAO):
    model = Player