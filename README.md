# SCRAPE FACEBOOK BIRTHDAYS TO PRIVATE GOOGLE CALENDAR
Python script to scrape birthdays of Facebook contacts to a private, manageable Google calendar. Scrape every birthday, or choose only the friends you would like.

1. Scrape birthdays from Facebook's .ics file. Read [here](https://www.anirudhsethi.in/blog/tech/import-facebook-birthdays-as-calendar/) how to access it.
2. **OPTIONAL**: Choose which friends you want to add to your calendar. It is possible to fetch everyone as well. 
3. A private calendar is created on your Google account with the birthday's you want to include.

## USAGE
Run **fb_birthdays.py**.

## IMPORTANT
* You need to add the [Google Calendar API credentials](https://developers.google.com/calendar/quickstart/python) to the same directory as the python files. 
* The URL for Facebook's calendar file must be placed in a text file called **"facebook_calendar.txt"** in the same directory as the python files.
* This script was made with the Swedish language in mind. Most changes for another language can be made at the top of the **"google_calendar.py"**.
* Line 73 in **"fb_birthdays.py"** is based on the Swedish language as well. It removes the facebook greeting after the name. Other languages can either remove the line or just change the variable.

## INFORMATION
* The birthday is set at *00:00* at morning.
* The birthday reoccurs **every year** at the same time.
* A reminder is set **10 days** before the birthday, as well as **1 day** before.
* Change the name of the calendar and the time zone at the top of the **"google_calendar.py"** file.
