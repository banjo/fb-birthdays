import requests

url = "https://www.facebook.com/events/ical/birthdays/?uid=1386784203&key=AQCzvWatSQFq7vql"


def main():
    data = get_data()
    data_list = data_to_list(data)
    data_dict = get_dict_from_list(data_list)
    # TODO: Add option to select which ones to add

    # TODO: Add to calendar


def get_dict_from_list(data_list):
    dictionary = {}  # init dictionary

    for text in data_list:
        # Birthdate
        birthday = text[10:18]

        # Name
        splitted = text.split("\n")
        long_name = splitted[2]
        name = long_name.replace("SUMMARY:", "")
        name = name.replace(" fyller år", "")
        name = name.replace("\r", "")

        # create tuple
        person_data = (name, birthday)

        # put into dictionary
        dictionary[name] = person_data

    input(len(dictionary))
    return dictionary


def data_to_list(data):
    new_data = data.split("BEGIN:VEVENT")
    new_data.pop(0)
    return new_data


def get_data():
    data = requests.get(url)
    return data.text


if __name__ == "__main__":
    main()
