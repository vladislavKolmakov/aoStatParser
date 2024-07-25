import asyncio
import pprint
import json

from src.ao_event_parser import Event_parser
from src.dao import EventDAO
from src.shemas import SEvent

def main():
    mock_data = open('mock_data.json', 'r').read()
    mock_data = json.loads(mock_data)

    while True:
        try:
            recent_events = Event_parser.get_recent_events()
        except Exception:
            print(Exception)
        for event in recent_events:
            
            event_info = {
                'event_id': event['EventId'],
                'time': Event_parser.prepare_date(event['TimeStamp']),
                'group_member_count': event['groupMemberCount'],
                'gvg_match': event['GvGMatch'],
                'kill_area': event['KillArea'],
            }

            killer = {
                'name': event['Killer']['Name'],
                'guild_name': event['Killer']['GuildName'],
                'alliance_name': event['Killer']['AllianceName'],
                'kill_fame': event['Killer']['KillFame'],
                'average_item_power': event['Killer']['AverageItemPower'],
                'main_hand': event['Killer']['Equipment']['MainHand']['Type'] if event['Killer']['Equipment']['MainHand'] is not None else None,
                'off_hand': event['Killer']['Equipment']['OffHand']['Type'] if event['Killer']['Equipment']['OffHand'] is not None else None,
                'head': event['Killer']['Equipment']['Head']['Type'] if event['Killer']['Equipment']['Head'] is not None else None,
                'armor': event['Killer']['Equipment']['Armor']['Type'] if event['Killer']['Equipment']['Armor'] is not None else None,
                'shoes': event['Killer']['Equipment']['Shoes']['Type'] if event['Killer']['Equipment']['Shoes'] is not None else None,
                'bag': event['Killer']['Equipment']['Bag']['Type'] if event['Killer']['Equipment']['Bag'] is not None else None,
                'cape': event['Killer']['Equipment']['Cape']['Type'] if event['Killer']['Equipment']['Cape'] is not None else None,
                'mount': event['Killer']['Equipment']['Mount']['Type'] if event['Killer']['Equipment']['Mount'] is not None else None,
                'potion': event['Killer']['Equipment']['Potion']['Type'] if event['Killer']['Equipment']['Potion'] is not None else None,
                'food': event['Killer']['Equipment']['Food']['Type'] if event['Killer']['Equipment']['Food'] is not None else None,
            }

            victim = {
                'name': event['Victim']['Name'],
                'guild_name': event['Victim']['GuildName'],
                'alliance_name': event['Victim']['AllianceName'],
                'kill_fame': event['Victim']['KillFame'],
                'average_item_power': event['Victim']['AverageItemPower'],
                'main_hand': event['Victim']['Equipment']['MainHand']['Type'] if event['Victim']['Equipment']['MainHand'] is not None else None,
                'off_hand': event['Victim']['Equipment']['OffHand']['Type'] if event['Victim']['Equipment']['OffHand'] is not None else None,
                'head': event['Victim']['Equipment']['Head']['Type'] if event['Victim']['Equipment']['Head'] is not None else None,
                'armor': event['Victim']['Equipment']['Armor']['Type'] if event['Victim']['Equipment']['Armor'] is not None else None,
                'shoes': event['Victim']['Equipment']['Shoes']['Type'] if event['Victim']['Equipment']['Shoes'] is not None else None,
                'bag': event['Victim']['Equipment']['Bag']['Type'] if event['Victim']['Equipment']['Bag'] is not None else None,
                'cape': event['Victim']['Equipment']['Cape']['Type'] if event['Victim']['Equipment']['Cape'] is not None else None,
                'mount': event['Victim']['Equipment']['Mount']['Type'] if event['Victim']['Equipment']['Mount'] is not None else None,
                'potion': event['Victim']['Equipment']['Potion']['Type'] if event['Victim']['Equipment']['Potion'] is not None else None,
                'food': event['Victim']['Equipment']['Food']['Type'] if event['Victim']['Equipment']['Food'] is not None else None,
            }
            
            loop = asyncio.get_event_loop()
            loop.run_until_complete(EventDAO.insert_if_not_exist(event_info, killer, victim))



if __name__ == "__main__":
    main()