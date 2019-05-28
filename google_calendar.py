from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # look for current calendars
    page_token = None
    calendar_exists = False

    calendar_list = service.calendarList().list(pageToken=page_token).execute()
    for calander_list_entry in calendar_list['items']:
        if "FB-Birthdays" in calander_list_entry["summary"]:
            print("""There is a calendar with that name. 
            Remove it or change the name.""")
            calendar_exists = True

    input("Paus")

    # create calendar
    calendar = {
        'summary': 'FB-Birthdays'
    }

    # if the calendar already exists, skip.
    if not calendar_exists:
        created_calendar = service.calendars().insert(body=calendar).execute()


if __name__ == '__main__':
    main()
