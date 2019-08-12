# Facebook Birthday to Gmail

A python script to scrape birthday dates from Facebook contacts. The will be added to a local Google Calendar. Choose all of your friends, or pick the ones you would like to save.

## Installation

-   Install [Python](https://www.python.org/) and [Git](https://git-scm.com/)
-   Download repository from Github

```bash
# Clone repository
$ git clone https://github.com/banjoanton/fb-birthdays.git

# Change directory to repository
$ cd "fb-birthdays"

# Install requirements
$ pip install -r requirements.txt
# or pip3 in some cases
$ pip3 install -r requirements.txt
```

-   Add [Calendar API credentials](https://developers.google.com/calendar/quickstart/pytho) to directory.
-   Get the Facebook `.ics` url adress ([guide here](https://www.anirudhsethi.in/blog/tech/import-facebook-birthdays-as-calendar/)). It contains all your contacts birthdays. Add it to `facebook_calendar.txt`.

## Usage

Run `fb_birthdays.py`


## Important
-   The URL for Facebook's calendar file must be placed in a text file called `facebook_calendar.txt` in root directory.
-   This script was made with the Swedish language in mind. Most changes for another language can be made at the top of the `google_calendar.py`.
-   Line 73 in `fb_birthdays.py` is based on the Swedish language as well. It removes the facebook greeting after the name. Other languages can either remove the line or just change the variable.

## Information

-   The birthday is set at `00:00` at morning.
-   The birthday reoccurs **every year** at the same time.
-   A reminder is set **10 days** before the birthday, as well as **1 day** before.
-   Change the name of the calendar and the time zone at the top of the `google_calendar.py` file.
