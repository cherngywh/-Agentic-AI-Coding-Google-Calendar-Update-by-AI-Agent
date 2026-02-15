# Google Calendar Tutoring Sessions

This project contains scripts and files to add tutoring sessions to Google Calendar with automatic email invitations and Zoom links.

> **Placeholders:** Replace `[ATTENDEE_1_EMAIL]`, `[ATTENDEE_2_EMAIL]`, `[TUTOR_NAME]`, `[CHILD_NAME_1]`, `[CHILD_NAME_2]`, `[YOUR_ZOOM_MEETING_LINK]`, and `[PROJECT_FOLDER]` with your actual values in the scripts.

## Files

| File | Purpose |
|------|---------|
| `add_to_google_calendar.py` | Main script — adds sessions to Google Calendar and sends invites |
| `tutoring_sessions.ics` | iCal file for manual import (backup) |
| `credentials.json` | OAuth credentials (create during setup) |
| `token.json` | Saved auth (auto-created on first run) |
| `SETUP_INSTRUCTIONS.md` | Google Calendar API setup guide |

## Quick Start

### Option 1: Automated Script (Recommended)

1. **Install required packages:**
   ```bash
   pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

2. **Set up Google Calendar API:**
   - Follow instructions in `SETUP_INSTRUCTIONS.md`
   - Download `credentials.json` and place it in this folder

3. **Run the script:**
   ```bash
   cd "[PROJECT_FOLDER]"
   python3 add_to_google_calendar.py
   ```

### Option 2: Manual Import (iCal)

1. Open Google Calendar (calendar.google.com)
2. Click "+" → "Import"
3. Select `tutoring_sessions.ics`
4. Manually add guests: `[ATTENDEE_1_EMAIL]` and `[ATTENDEE_2_EMAIL]`

## Session Details

- **Total Sessions:** 12
- **Date Range:** February 15, 2026 - April 7, 2026
- **Subjects:** Elementary Reading, Elementary Writing Composition
- **Tutors:** [TUTOR_NAME]
- **Children:** [CHILD_NAME_1], [CHILD_NAME_2]
- **Zoom Link:** [YOUR_ZOOM_MEETING_LINK]
- **Attendees:** [ATTENDEE_1_EMAIL], [ATTENDEE_2_EMAIL]

## Cost

**FREE** - Google Calendar API is free for personal use. No charges apply.

## Notes

- All sessions are set to Pacific Time (PST/PDT)
- Zoom link is included in all event descriptions
- Email reminders: 1 day before and 15 minutes before each session
- Invitations will be sent automatically when using the Python script
