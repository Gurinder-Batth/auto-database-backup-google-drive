from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import os 



gauth = GoogleAuth()
scope = ["https://www.googleapis.com/auth/drive"]
JSON_FILE = "./editor.json"
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE, scope)
drive = GoogleDrive(gauth)


path = "./sql"
folder_id = "1cz3WQ4M5zVXInJfOEdvwn09ZUJogAMKD" # Replace with the actual folder ID or set to None for the root directory
parent_folder_id = "1cz3WQ4M5zVXInJfOEdvwn09ZUJogAMKD"

query = f"'{folder_id}' in parents" if folder_id else "'root' in parents"
file_list = drive.ListFile({'q': query}).GetList()
print(file_list)
# Print the details of each file
for file in file_list:
    print(f"Title: {file['title']}, ID: {file['id']}")


# # iterating thought all the files/folder 
# # of the desired directory 
for x in os.listdir(path):
    file_path = os.path.join(path, x)

    # Check if the item is a file (not a directory)
    if os.path.isfile(file_path):
        # Create GoogleDriveFile instance
        file_drive = drive.CreateFile({'title': x})

        # Set content of the file from the local file
        file_drive.SetContentFile(file_path)

        # Set the parent folder after creating the file
        if parent_folder_id:
            file_drive['parents'] = [{'id': parent_folder_id}]

        # Upload the file
        file_drive.Upload()

        print(f"File '{file_path}' uploaded to Google Drive")
        authenticated_user_email = gauth.credentials.service_account_email
        print(f"File uploaded to Google Drive by {authenticated_user_email}")
        # Close the file to prevent memory leaks
        file_drive = None