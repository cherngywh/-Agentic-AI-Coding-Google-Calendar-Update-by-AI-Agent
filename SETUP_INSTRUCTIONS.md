# Google Calendar API Setup Instructions

Follow these steps to set up the Google Calendar API for automated event creation.

## Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the project dropdown at the top
3. Click "New Project"
4. Enter a project name (e.g., "Tutoring Calendar")
5. Click "Create"

## Step 2: Enable Google Calendar API

1. In the Google Cloud Console, go to "APIs & Services" → "Library"
2. Search for "Google Calendar API"
3. Click on "Google Calendar API"
4. Click "Enable"

## Step 3: Create OAuth 2.0 Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure the OAuth consent screen:
   - Choose "External" (unless you have a Google Workspace account)
   - Fill in the required fields:
     - App name: "Tutoring Calendar Manager"
     - User support email: Your email
     - Developer contact: Your email
   - Click "Save and Continue"
   - Add scopes: `https://www.googleapis.com/auth/calendar`
   - Click "Save and Continue"
   - Add test users (optional for now)
   - Click "Save and Continue"
   - Review and click "Back to Dashboard"

4. Create OAuth Client ID:
   - Application type: "Desktop app"
   - Name: "Tutoring Calendar Client"
   - Click "Create"

5. Download the credentials:
   - Click the download icon (⬇) next to your newly created OAuth client
   - Save the file as `credentials.json`
   - **Move `credentials.json` to this folder:** `[PROJECT_FOLDER]/`

## Step 4: Install Python Packages

```bash
pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Step 5: Run the Script

```bash
cd "/Users/cherngywhlee/Work/Google Calendar Tutoring Sessions"
python3 add_to_google_calendar.py
```

### First Run

1. The script will open a browser window
2. Sign in with your Google account
3. Grant permissions to access your Google Calendar
4. The script will save a `token.json` file for future use
5. All 12 sessions will be added to your calendar
6. Email invitations will be sent automatically

### Subsequent Runs

- The script will use the saved `token.json` file
- No browser login required (unless token expires)

## Troubleshooting

### "credentials.json not found"
- Make sure you downloaded the OAuth credentials file
- Rename it to exactly `credentials.json`
- Place it in the same folder as `add_to_google_calendar.py`

### "Permission denied" or "Access denied"
- Make sure you enabled Google Calendar API
- Check that you granted the correct permissions during OAuth flow
- Try deleting `token.json` and running again

### "Quota exceeded"
- This is very unlikely for 12 events
- If it happens, wait a few minutes and try again
- Free tier allows 1,000,000 requests per day

## Security Notes

- Keep `credentials.json` and `token.json` private
- Don't commit these files to public repositories
- They're already in `.gitignore` if using git

## Cost

**FREE** - No charges for Google Calendar API usage in this project.
