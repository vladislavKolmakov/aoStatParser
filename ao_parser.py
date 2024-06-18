import requests
import json

class Parser:
    @staticmethod
    def get_event_data(event_id):
        url = f"https://gameinfo.albiononline.com/api/gameinfo/events/{event_id}"

        event_data = requests.get(url)

        return json.loads(event_data.content)
        # return json.load(event_data.text)

    @staticmethod
    def parse_player_data():
        pass