# DROP TABLES

songplay_table_drop = "DROP TABLE songplays;"
user_table_drop = "DROP TABLE users;"
song_table_drop = "DROP TABLE songs;"
artist_table_drop = "DROP TABLE artists;"
time_table_drop = "DROP TABLE times;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
    (
        songplay_id SERIAL PRIMARY KEY,
        start_time  timestamp NOT NULL, 
        user_id     int  NOT NULL, 
        level       varchar NOT NULL, 
        song_id     varchar, 
        artist_id   varchar, 
        session_id  varchar NOT NULL, 
        location    VARCHAR  NOT NULL, 
        user_agent  VARCHAR  NOT NULL
    );
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
    (
        user_id    int PRIMARY KEY,
        first_name varchar,
        last_name  varchar, 
        gender     varchar, 
        level      varchar
    );
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
    (
        song_id   varchar PRIMARY KEY, 
        title     varchar NOT NULL, 
        artist_id varchar NOT NULL, 
        year      int NOT NULL, 
        duration  float NOT NULL
    );
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
    (
        artist_id varchar primary key not null, 
        name      varchar not null, 
        location  varchar, 
        latitude  float, 
        longitude float
    );
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS times
    (
        time_id    SERIAL PRIMARY KEY, 
        start_time timestamp NOT NULL, 
        hour       varchar NOT NULL, 
        day        varchar NOT NULL, 
        week       varchar NOT NULL, 
        month      varchar NOT NULL, 
        year       int NOT NULL, 
        weekday    varchar NOT NULL
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING; 
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (user_id) 
    DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_insert = ("""
INSERT INTO times (start_time, hour, day, week, month, year, weekday) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, songs.artist_id 
FROM songs JOIN artists ON songs.artist_id = artists.artist_id 
WHERE (%s = songs.title) AND (%s = artists.name) AND (%s = songs.duration);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]