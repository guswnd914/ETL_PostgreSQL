# Developing ETL by Python and PostgreSQL Modeling
******************************************************************
This is originally a project hosted by Udacity and had been edited for its structure and style due to my preference.
Working for this project mainly taught me three things :
* Data modeling with PostgreSQL
* Database star schema created
* ETL pipeline using Python

## Context
*************************************
There are two given JSON-format meta-datasets : "song_data" and "log_data".
"song_data" is factual information about songs whereas "log_data" is a collection of user activities in a music application.
These two datasets seem to be well-connected and are worthy to be analyzed by smart analytics team.
Yet, since these data are not arranged properly to each other, it becomes practically impossible to analyze them; it's a huge problem.
And my goal is to solve this problem by creating a efficent database schema so that the data can be easily analyzed by other analysts.
### Data

- **song_data** : all json files are nested in subdirectories under /data/song_data. A sample of this files is:
`{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}`

- **log_data** : all json files are nested in subdirectories under /data/log_data. A sample of a single row of each files is:
`{"artist":"Slipknot","auth":"Logged In","firstName":"Aiden","gender":"M","itemInSession":0,"lastName":"Ramirez","length":192.57424,"level":"paid","location":"New York-Newark-Jersey City, NY-NJ-PA","method":"PUT","page":"NextSong","registration":1540283578796.0,"sessionId":19,"song":"Opium Of The People (Album Version)","status":200,"ts":1541639510796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.1) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"20"}`

### Database Schema

### Fact Table
#### songplays - records in log data associated with song plays i.e. records with page NextSong

- songplay_id (INT) PRIMARY KEY: ID of each user song play
- start_time (DATE) NOT NULL: Timestamp of beggining of user activity
- user_id (INT) NOT NULL: ID of user
- level (TEXT): User level {free | paid}
- song_id (TEXT) NOT NULL: ID of Song played
- artist_id (TEXT) NOT NULL: ID of Artist of the song played
- session_id (INT): ID of the user Session
- location (TEXT): User location
- user_agent (TEXT): Agent used by user to access Sparkify platform

### Dimension Tables
#### users - users in the app

- user_id (INT) PRIMARY KEY: ID of user
- first_name (TEXT) NOT NULL: Name of user
- last_name (TEXT) NOT NULL: Last Name of user
- gender (TEXT): Gender of user {M | F}
- level (TEXT): User level {free | paid}
- songs - songs in music database

#### song_id (TEXT) PRIMARY KEY: ID of Song
- title (TEXT) NOT NULL: Title of Song
- artist_id (TEXT) NOT NULL: ID of song Artist
- year (INT): Year of song release
- duration (FLOAT) NOT NULL: Song duration in milliseconds
- artists - artists in music database

#### artist_id (TEXT) PRIMARY KEY: ID of Artist
- name (TEXT) NOT NULL: Name of Artist
- location (TEXT): Name of Artist city
- lattitude (FLOAT): Lattitude location of artist
- longitude (FLOAT): Longitude location of artist

#### time (TIMESTAMP) : timestamps of records in songplays broken down into specific units
- start_time (DATE) PRIMARY KEY: Timestamp of row
- hour (INT): Hour associated to start_time
- day (INT): Day associated to start_time
- week (INT): Week of year associated to start_time
- month (INT): Month associated to start_time
- year (INT): Year associated to start_time
- weekday (TEXT): Name of week day associated to start_time

## How it works?
***************************************************************
Create any note and code "%run create_tables.py" and then "%run etl.py"
Then all the data from the datasets will be stored into the data pipeline.

## Contents : 
***********************************************************************

**data** - It is a subset of "Million Song Dataset". The original dataset is known to have 280GB memory! It consists of huge features related to songs (ex. song_name, artist, artist_id, time, duration, etc...)

**create_tables.py** - It functions to create database through connecting to PostgreSQL and also features itself with "Create_tables" and "Drop_tables" functions. It imports SQL queries from "sql_queries.py" and perform its functions.
                       
**etl.ipynb** - It is a procedure sketch to build etl.py's contents. It first creates function, "get_files", to get files from the current directories and then get two major data, which are "song_data" and "log_data". From these data, I extracted line-by-line information, wrangled with my own personal preference, and then loaded them to our database within 5 tables.

**etl.py** - It is the automation of "etl.ipynb". Just running this file, our database is loaded with the data.

**sql_queries.py** - It is a list of SQL queries especially in dropping tables, creating tables, inserting tables, and finding songs.

**test.ipynb** - It tests to see if our data pipeline works or not.


# Thank you!
