import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *




def process_song_file(cur, filepath):
    """
    This function makes extraction from song_data
    and load to songs and artists tables
    in the assigned PostgreSQL database.
    """
    # user defined function for getting values from the column
    def get_val(col_name):
        index = list(df.columns).index(col_name)
        return df.values[0][index]
    
    # converts the file to dataframe
    df = pd.read_json(filepath, lines=True)
    
    
    # inserting song info to songs table.
    song_data = [get_val('song_id'), get_val('title'), 
                 get_val('artist_id'), get_val('year'), get_val('duration')]
    cur.execute(song_table_insert, song_data)
    
    # inserting artist info to artists table.
    artist_data = [get_val('artist_id'), get_val('artist_name'), get_val('artist_location'), 
                   get_val('artist_latitude'), get_val('artist_longitude')]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    This function makes extraction from log_data
    and load to time, users, and songplays tables
    in the assigned PostgreSQL database.
    """

    # ETL on time table
    df = df.query('page == "NextSong"')
    t = pd.to_datetime(df.ts, unit='ms')
    time_data = (t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.day_name())
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_dict = dict(zip(column_labels, time_data))
    time_df = pd.DataFrame.from_dict(time_dict)
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # ETL on users table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # ETL on songplays table
    for index, row in df.iterrows():
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
            
        # inserting songplay record
        songplay_data = songplay_data = (index, t[index], row.userId, row.level, 
                                         songid, artistid, row.sessionId, row.location, row.userAgent )
        cur.execute(songplay_table_insert, songplay_data)



def process_data(cur, conn, filepath, func):
    """
    This function makes retrieval of datasets in the filepath
    and informs extraction processes
    by printing numbers of files found
    and by printing numbers of files processed
    """
    
    # retrieval of datasets in the directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # print amount of files found over total amount
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # print amount of files processed over total amount
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))



def main():
    """
    This main function makes connection to PostgreSQL database
    and assigns cursor from the connection.
    Then it extracts data from all datasets within the directory
    and load them to the assigned PostgreSQL database.
    """
    
    # Connection to PosgreSQL DB and its cursor
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    # ETL process
    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()