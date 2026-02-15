#!/usr/bin/env python3
"""
Script to add tutoring sessions to Google Calendar using Google Calendar API.
Requires: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""

import os
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Tutoring sessions data
SESSIONS = [
    {
        'date': '2026-02-15',
        'time_start': '12:00',
        'time_end': '13:00',
        'subject': 'Elementary Reading',
        'tutor': 'Sid L.',
        'child': 'Meredith Soleyjacks',
        'location': 'Online Session'
    },
    {
        'date': '2026-02-17',
        'time_start': '16:00',
        'time_end': '17:00',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-02-22',
        'time_start': '12:00',
        'time_end': '13:00',
        'subject': 'Elementary Reading',
        'tutor': 'Sid L.',
        'child': 'Meredith Soleyjacks',
        'location': 'Online Session'
    },
    {
        'date': '2026-02-27',
        'time_start': '15:00',
        'time_end': '16:00',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-03-13',
        'time_start': '15:00',
        'time_end': '16:00',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-03-17',
        'time_start': '16:00',
        'time_end': '17:00',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-03-20',
        'time_start': '15:00',
        'time_end': '16:00',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-03-25',
        'time_start': '14:30',
        'time_end': '15:30',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-03-27',
        'time_start': '15:00',
        'time_end': '16:00',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-04-01',
        'time_start': '14:30',
        'time_end': '15:30',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-04-03',
        'time_start': '15:00',
        'time_end': '16:00',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
    {
        'date': '2026-04-07',
        'time_start': '16:00',
        'time_end': '17:00',
        'subject': 'Elementary Writing Composition',
        'tutor': 'Sid L.',
        'child': 'Grace Johnson',
        'location': 'Online Session'
    },
]

ZOOM_LINK = "https://us02web.zoom.us/j/81931997718"
ATTENDEES = ["tsou819111@gmail.com", "leesid0201@gmail.com"]

def get_calendar_service():
    """Authenticate and return Google Calendar service."""
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("Error: credentials.json not found!")
                print("Please download it from Google Cloud Console:")
                print("1. Go to https://console.cloud.google.com/")
                print("2. Create a project and enable Google Calendar API")
                print("3. Create OAuth 2.0 credentials")
                print("4. Download as credentials.json")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return build('calendar', 'v3', credentials=creds)

def create_event(service, session):
    """Create a calendar event for a tutoring session."""
    # Parse date and time
    date_str = session['date']
    start_time = session['time_start']
    end_time = session['time_end']
    
    # Create datetime objects (assuming PST timezone, adjust as needed)
    start_datetime = datetime.strptime(f"{date_str} {start_time}", "%Y-%m-%d %H:%M")
    end_datetime = datetime.strptime(f"{date_str} {end_time}", "%Y-%m-%d %H:%M")
    
    # Format for Google Calendar API (RFC3339 format)
    start_rfc3339 = start_datetime.strftime("%Y-%m-%dT%H:%M:00-08:00")  # PST
    end_rfc3339 = end_datetime.strftime("%Y-%m-%dT%H:%M:00-08:00")  # PST
    
    event = {
        'summary': f"{session['subject']} - {session['tutor']} with {session['child']}",
        'description': f"Subject: {session['subject']}\nTutor: {session['tutor']}\nChild: {session['child']}\nLocation: {session['location']}\n\nZoom Link: {ZOOM_LINK}",
        'location': session['location'],
        'start': {
            'dateTime': start_rfc3339,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_rfc3339,
            'timeZone': 'America/Los_Angeles',
        },
        'attendees': [{'email': email} for email in ATTENDEES],
        'conferenceData': {
            'createRequest': {
                'requestId': f"zoom-{session['date']}-{start_time.replace(':', '')}",
                'conferenceSolutionKey': {'type': 'hangoutsMeet'},
            }
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},  # 1 day before
                {'method': 'popup', 'minutes': 15},  # 15 minutes before
            ],
        },
    }
    
    # Add Zoom link as a custom property
    event['extendedProperties'] = {
        'private': {
            'zoomLink': ZOOM_LINK
        }
    }
    
    # Add Zoom link to description if conference data doesn't work
    event['description'] += f"\n\nJoin Zoom Meeting: {ZOOM_LINK}"
    
    try:
        event = service.events().insert(calendarId='primary', body=event, sendUpdates='all').execute()
        print(f"✓ Created event: {event.get('summary')} on {session['date']}")
        return event
    except HttpError as error:
        print(f"✗ An error occurred: {error}")
        return None

def main():
    """Main function to add all sessions to Google Calendar."""
    print("Connecting to Google Calendar...")
    service = get_calendar_service()
    
    if not service:
        print("\nPlease set up Google Calendar API credentials first.")
        print("See instructions in the script comments.")
        return
    
    print(f"\nAdding {len(SESSIONS)} tutoring sessions to Google Calendar...")
    print("=" * 60)
    
    created_count = 0
    for session in SESSIONS:
        event = create_event(service, session)
        if event:
            created_count += 1
    
    print("=" * 60)
    print(f"\n✓ Successfully added {created_count} out of {len(SESSIONS)} sessions to Google Calendar")
    print(f"✓ Invitations sent to: {', '.join(ATTENDEES)}")
    print(f"✓ Zoom link added to all events: {ZOOM_LINK}")

if __name__ == '__main__':
    main()
