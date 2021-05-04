# Data Warehouse Project

## Project Background

Sparkify is a music streaming startup. It has a growing user base and song database and wants to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

This projects will build an ETL pipeline that extracts data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for the analytics team to continue finding insights in what songs their users are listening to.

## Files

- README.md
introduce project background, how to run files, and database schema structure
- dwh.cfg
login and access information for AWS, S3, RedShift
- sql_queries.py
sql queries used to drop/create staging tables, dimention tables, fact tables, and analytical test queries
- create_tables.py
python script to use the modules in sql_queries.py to create/drop tables in RedShift
- etl.py
python script to use the modules in sql_queries.py to load data from S3 to staging tables in RedShift, then insert data into final tables

## How to run

1. Create a Redshift cluster first in AWS website and create an IAM role with S3 access for Reshift
2. Add the cluster details in the *dwh.cfg* file
3. Run *create_tables.py* to set up the staging and analytical tables
    `python create_tables.py`
4. Then run *etl.py* to extract files in S3, stage it in Redshift, and store it in the dimensional tables
    `python etl.py`
    
## Database schema design

### Staging tables
follow the same structure of the data souce
- staging_events
- staging_songs

###  Fact Table
- songplays: _records in event data associated with song plays i.e. records with page NextSong_
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
- users _users in the app_
user_id, first_name, last_name, gender, level
- songs _songs in music database_ 
song_id, title, artist_id, year, duration
- artists _artists in music database_
artist_id, name, location, lattitude, longitude
- time _timestamps of records in songplays broken down into specific units_ 
start_time, hour, day, week, month, year, weekday
