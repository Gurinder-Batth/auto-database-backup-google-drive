#!/bin/bash

# Container ID
container_id="755ac94582e6"

# MySQL credentials
mysql_user="root"
mysql_password="password"
database_name="laravel"

# Backup directory inside the container
backup_dir=""

# Local directory to store the backup
local_backup_dir="./"

# Get current date for the backup file
backup_date=$(date +"%Y%m%d_%H%M%S")
backup_file="${database_name}_backup_${backup_date}.sql"

# Step 1: Run MySQL command inside the Docker container to take a backup
docker exec -i "$container_id" mysqldump -u"$mysql_user" -p"$mysql_password" "$database_name" > "./sql/$backup_file"