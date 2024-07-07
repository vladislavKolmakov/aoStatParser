from sqlalchemy import Column, Integer, String, DateTime, Boolean
from src.database import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    killer_id = Column(Integer)
    victim_id = Column(Integer)
    time = Column(DateTime)
    group_member_count = Column(Integer)
    gvg_match = Column(Boolean)
    kill_area = Column(String)


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    guild_name = Column(String)
    alliance_name = Column(String)
    kill_fame = Column(String)
    average_itemPower = Column(Integer)
    main_Hand = Column(String)
    off_hand = Column(String)
    head = Column(String)
    armor = Column(String)
    shoes = Column(String)
    bag = Column(String)
    cape = Column(String)
    mount = Column(String)
    potion = Column(String)
    food = Column(String)
