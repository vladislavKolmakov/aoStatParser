from sqlalchemy import delete, insert, select, text
from sqlalchemy.exc import SQLAlchemyError

from src.database import async_session_maker
from src.models import Event, Player
from src.shemas import SEvent, SPlayer

class BaseDAO:
    model = None

    @classmethod
    async def get_by_filter(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)

            return result.fetchall()
    
    
    @classmethod
    async def insert(cls, **data):
        try:
            async with async_session_maker() as session:
                query = insert(cls.model).values(**data)
                result = await session.execute(query)
                await session.commit()
                inserted_id = result.inserted_primary_key
                return inserted_id
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc: Cannot insert data into table"
            elif isinstance(e, Exception):
                msg = "Unknown Exc: Cannot insert data into table"

            print(e, msg)
            return None


class EventDAO(BaseDAO):
    model = Event

    @classmethod
    async def insert_if_not_exist(cls, event: SEvent, killer: SPlayer, victim: SPlayer):
        async with async_session_maker() as session:
            is_exists = await cls.get_by_filter(**{"event_id": event['event_id']})
            is_exists = True if is_exists != [] else False
            if not is_exists:
                victim_id = await PlayerDAO.insert(**victim)
                killer_id = await PlayerDAO.insert(**killer)

                event['killer_id'] = killer_id[0]
                event['victim_id'] = victim_id[0]
                await cls.insert(**event)
            return is_exists


class PlayerDAO(BaseDAO):
    model = Player
