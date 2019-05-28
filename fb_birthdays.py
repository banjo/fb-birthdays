import requests
import google_calendar
import datetime

# read facebook calendar url from file for privacy
with open("./facebook_calendar.txt", "r") as f:
    url = f.read()


def main():
    data = get_data()
    data_list = data_to_list(data)
    birthday_dict = get_dict_from_list(data_list)

    # choose birthdays
    birthday_dict = choose_birthdays(birthday_dict)

    # Add to calendar
    google_calendar.main(birthday_dict)


def choose_birthdays(birthday_dict):
    while True:
        answer = input(
            "Do you want to choose which birthdays to include? (y/n) ")

        if answer.lower() == "n":
            return birthday_dict
        elif answer.lower() == "y":
            choosen_birthdays = get_birthdays(birthday_dict)
            return choosen_birthdays
        else:
            continue


def get_birthdays(birthday_dict):
    #  create temporary dict to return
    temp = {}

    #  print information
    input("The names will be printed, include by pressing 'y', exclude by pressing Enter. Press Enter when you are ready. ")

    for key in birthday_dict:
        name, birthday = birthday_dict[key]
        answer = input(f"{name} ")

        if answer.lower() == "y":
            temp[name] = birthday_dict[key]

    return temp


def get_dict_from_list(data_list):
    dictionary = {}  # init dictionary

    for text in data_list:
        # Birthdate
        birthday = text[10:18]
        year, month, day = birthday[:4], birthday[4:6], birthday[6:8]

        # remove first 0 in month
        if str(month).startswith("0"):
            month = int(str(month).replace("0", ""))

        # get correct format
        birthday = datetime.datetime(
            int(year), int(month), int(day), 00, 00, 00, 00).isoformat()

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

    return dictionary


def data_to_list(data):
    print("Creating list...")
    new_data = data.split("BEGIN:VEVENT")
    new_data.pop(0)
    return new_data


def get_data():
    print("Downloading data...")
    data = requests.get(url)
    return data.text


if __name__ == "__main__":
    main()
