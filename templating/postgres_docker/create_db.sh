#!/bin/sh

psql -U postgres
psql --command "CREATE USER user WITH PASSWORD 'userpassword';" 
psql --command "CREATE DATABASE userdb;"
psql --command "GRANT ALL PRIVILEGES ON DATABASE userdb to user;"
psql --command "\q;"  
psql -U user -d userdb -f /var/lib/postgresql/backup.sql

exit