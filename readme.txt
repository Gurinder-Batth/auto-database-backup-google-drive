# Google Drive Database Backup Automation

Author: Gurinderpal Singh

This readme.txt file provides a simplified version of the instructions on how to set up an automated process to store a daily backup of your production database on Google Drive using a simple bash script and a Python script. The Python script utilizes a Google Cloud service account, which is free of cost. This process involves creating a folder in your Google Drive and granting access to the service account by sending an invitation to its email address. A cron job is then set up to execute the Python and bash scripts every 24 hours.

## Prerequisites

Before you begin, make sure you have the following prerequisites:

1. **Google Cloud Service Account**: Create a service account on the Google Cloud Console. This account will be used to interact with Google Drive. Make sure to download the JSON key file for this service account.

2. **Google Drive**: Access to a Google Drive account where you want to store your database backups. You will create a folder specifically for these backups.

3. **MySQL Database**: Ensure you have a MySQL database that you want to back up.

4. **Python**: Python should be installed on your system to run the Python script.

## Setup Steps

Follow these simplified steps to set up the automated Google Drive database backup:

### 1. Create a Google Drive Folder

1. Log in to your Google Drive account.

2. Create a new folder named "DatabaseBackups" (or a name of your choice) to store the database backups.

### 2. Share Folder with Service Account

1. Right-click on the "DatabaseBackups" folder and select "Share."

2. In the sharing dialog, enter the email address associated with your Google Cloud service account.

3. Set the service account's access level to "Editor" or "Viewer," depending on your preference.

4. Click "Send" to send an invitation to the service account's email address.

### 3. Clone or Download Scripts

Clone this repository or download the two scripts: `backup_script.sh` (bash script) and `upload_to_drive.py` (Python script).

### 4. Configure the Scripts

1. Open `backup_script.sh` and set the MySQL database credentials (username and password) and adjust the backup file name and location as needed.

2. Open `upload_to_drive.py` and configure the file paths and Google Drive folder ID.

### 5. Test the Scripts

You can test the scripts manually to ensure they work correctly.

### 6. Set Up a Cron Job

Set up a cron job to schedule the backup and upload tasks to run every 24 hours.

### 7. Save and Exit

Save the changes to the cron job file and exit the text editor.

## Automation in Action

With these steps completed, your database will be automatically backed up to your Google Drive folder every day. You can check the Google Drive "DatabaseBackups" folder for the backups.

Make sure to monitor your backups and adjust the retention policy as needed to manage storage space efficiently.


