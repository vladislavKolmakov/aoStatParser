from src.ao_event_parser import Event_parser
import pprint

def main():
    # event_id = 1051418761

    # event_data = Event_parser.get_event_data(event_id)
    # event_info = Event_parser.parse_event_info(event_data)
    # victim_info = Event_parser.parse_player_data(event_data, 'victim')
    # killer_info = Event_parser.parse_player_data(event_data, 'killer')

    # pprint.pp(event_info)
    # pprint.pp(victim_info)
    # pprint.pp(killer_info)

    recent_events = Event_parser.get_recent_events()
    for event in recent_events:
        print(event['EventId'])
    # pprint.pp(recent_events)



if __name__ == "__main__":
    main()