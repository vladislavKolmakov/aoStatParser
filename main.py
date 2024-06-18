from ao_parser import Parser

def main():
    event_id = 1051418761

    data = Parser.get_event_data(event_id)
    print(data)



if __name__ == "__main__":
    main()