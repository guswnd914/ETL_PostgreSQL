

Running the python scripts :
    Create any note and code "%run create_tables.py" and then "%run etl.py"
    Then all the data from the datasets will be stored into our ETL Data Pipeline.

Description :
    This ETL Data Pipeline is engined by PostgreSQL and is similar to snowflakes schema with 1 fact table, 4 dimension tables.
    The fact table is "song_play table".
    The dimension tables are "user_table", "song_table", "artist_table", and "time_table".


Contents :
"data" - It is subset of "Million Song Dataset". The original dataset is known to have 280GB memory! It consists of huge features related to songs (ex. song_name, artist, artist_id, time, duration, etc...)

"create_tables.py" - It functions to create database through connecting to PostgreSQL and also features itself with "Create_tables" and "Drop_tables" functions. It imports SQL queries from "sql_queries.py" and perform its functions.
                       
"etl.ipynb" - It is a procedure sketch to build etl.py's contents. It first creates function, "get_files", to get files from the current directories and then get two major data, which are "song_data" and "log_data". From these data, I extracted line-by-line information, wrangled with my own personal preference, and then loaded them to our database within 5 tables.

"etl.py" - It is the automation of "etl.ipynb". Just running this file, our database is loaded with the data.

"sql_queries.py" - It is a list of SQL queries especially in dropping tables, creating tables, inserting tables, and finding songs.

"test.ipynb" - It tests to see if our data pipeline works or not.
    
    # Data-Analysis
# Data-Analysis
