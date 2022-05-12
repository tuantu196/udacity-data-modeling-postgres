<h1>DATA MODELING WITH POSTGRESQL</h1>
<h2>Introduction<h2>
<p>A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.</p>

<p>They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.</p>
    
<h2>Project Description<h2>
<p>In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.<p>
    
<h2>How to run the Python scripts<h2>
<p>Open Terminal<p>
<p>python ***.py<p>
    
<h2>An explanation of the files in the repository<h2>
    
| File - Folder | Description |
| --- | ----------- |
| data | Raw datas store in here, log_data and song_data. |
| create_tables.py | Drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts. |
| etl.ipynb | Reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables. |
| etl.py | Reads and processes files from song_data and log_data and loads them into your tables. |    
| sql_queries.py | Contains all your sql queries, and is imported into the last three files above. |    
| test.ipynb | Displays the first few rows of each table to let you check your database. |