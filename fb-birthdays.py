import requests

url = "https://www.facebook.com/events/ical/birthdays/?uid=1386784203&key=AQCzvWatSQFq7vql"


def main():
    data = get_data()
    data_list = data_to_list(data)
    sorted_list = sort_list(data_list)


def sort_list(data_list):
    for text in data_list:
        input(text)


def data_to_list(data):
    new_data = data.split("BEGIN:VEVENT")
    new_data.pop(0)
    return new_data


def get_data():
    data = requests.get(url)
    return data.text


if __name__ == "__main__":
    main()
