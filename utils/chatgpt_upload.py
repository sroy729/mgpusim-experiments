import argparse
import pandas as pd
import os.path
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the scope and service account file
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './sheets_api/token.json'

def upload_csv_to_gsheet(csv_file, spreadsheet_id, sheet_name):
    # Authenticate and create the service
    creds = None
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Convert the DataFrame to a list of lists
        values = [df.columns.values.tolist()] + df.values.tolist()

        # Define the body of the request
        body = {
            'values': values
        }

        # Call the Sheets API to update the sheet
        sheet = service.spreadsheets()
        result = sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=sheet_name,
            valueInputOption="RAW",
            body=body
        ).execute()
        print(f"{result.get('updatedCells')} cells updated.")
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Upload CSV to Google Sheets')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('spreadsheet_id', help='Google Sheets spreadsheet ID')
    parser.add_argument('sheet_name', help='Name of the sheet within the spreadsheet')

    args = parser.parse_args()

    upload_csv_to_gsheet(args.csv_file, args.spreadsheet_id, args.sheet_name)

