from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class SEvent(BaseModel):
    id: Optional[int]
    event_id: int
    killer_id: int
    victim_id: int
    time: datetime
    group_member_count: int
    gvg_match: bool
    kill_area: str


class SPlayer(BaseModel):
    id: Optional[int]
    name: str
    guild_name: str
    alliance_name: str
    kill_fame: int
    average_itemPower: int
    main_Hand: str
    off_hand: str
    head: str
    armor: str
    shoes: str
    bag: str
    cape: str
    mount: str
    potion: str
    food: str