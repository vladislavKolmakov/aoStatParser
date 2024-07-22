from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EventDTO:
    event_id: int
    killer_id: int
    victim_id: int
    time: datetime
    group_member_count: int
    gvg_match: bool
    kill_area: str