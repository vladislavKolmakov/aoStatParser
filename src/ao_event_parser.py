import requests
import json

class Event_parser:
    @staticmethod
    def get_recent_events(limit: int = 10, offset: int = 0):
        url = f"https://gameinfo.albiononline.com/api/gameinfo/events?limit={limit}&offset={offset}"
        events = requests.get(url)

        return json.loads(events.content)

    @staticmethod
    def get_event_data(event_id: int):
        url = f"https://gameinfo.albiononline.com/api/gameinfo/events/{event_id}"

        event_data = requests.get(url)

        return json.loads(event_data.content)
        # return json.load(event_data.text)


    @staticmethod
    def parse_equip(equip: dict):
        res = {}
        for cell in equip:
            res[cell] = equip[cell]['Type'] if equip[cell] is not None else None
            # item_type = item_cell['Type']
            # enchantment = item_type.split('@')[1] if '@' in item_type else 0
            # quality = item_cell['Quality'] if item_cell['Quality'] is not None else None
            # res[item_cell] = item_type
        
        return res


    @staticmethod
    def parse_event_info(data):
        pricipant_data = {
            'groupMemberCount': data['groupMemberCount'],
            'event_id': data['EventId'],
            'time_stamp': data['TimeStamp'],
            'gvg_match': data['GvGMatch'],
            'kill_area': data['KillArea'],
        }

        return pricipant_data


    @staticmethod
    def parse_player_data(player_data: dict, pricipant_type):
        if pricipant_type == 'killer':
            pricipant = player_data['Killer']
        elif pricipant_type == 'victim':
            pricipant = player_data['Victim']

        pricipant_data = {
            'average_itemPower': pricipant['AverageItemPower'],
            # 'equip': pricipant['Equipment'],
            'equip': Event_parser.parse_equip(pricipant['Equipment']),
            'name': pricipant['Name'],
            'guild_name': pricipant['GuildName'],
            'alliance_name': pricipant['AllianceName'],
            'kill_fame': pricipant['KillFame'],
        }

        return pricipant_data
