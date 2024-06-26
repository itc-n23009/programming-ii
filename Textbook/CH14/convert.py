import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials-sheets.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def upload_and_convert(filename):
    service = build('drive', 'v3', credentials=get_credentials())
    file_metadata = {'name': os.path.basename(filename), 'mimeType': 'application/vnd.google-apps.spreadsheet'}
    media = MediaFileUpload(filename, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file['id']

def download_as(file_id, mime_type, output_filename):
    service = build('drive', 'v3', credentials=get_credentials())
    request = service.files().export_media(fileId=file_id, mimeType=mime_type)
    with open(output_filename, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
    print(f"File downloaded as {output_filename}")

def main():
    upload_file = '/home/vagrant/LibreOffice_7.6.7.2_Linux_x86-64_deb/DEBS/example.xlsx'
    if not os.path.exists(upload_file):
        print(f"Error: File '{upload_file}' not found.")
        return

    try:
        sheet_id = upload_and_convert(upload_file)
        print(f"Uploaded and converted to Google Sheets. Sheet ID: {sheet_id}")
        download_as(sheet_id, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'downloaded_excel.xlsx')
        download_as(sheet_id, 'application/x-vnd.oasis.opendocument.spreadsheet', 'downloaded_ods.ods')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
