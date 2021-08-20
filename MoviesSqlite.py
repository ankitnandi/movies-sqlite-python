import sqlite3
from sqlite3 import Error


def create_connection():
    try:
        connection = sqlite3.connect('movieDb.db')
        print("Connection to movie database is established")
        return connection
    except Error:
        print(Error)


def create_table(connection):
    check_and_drop_table_if_exists(connection)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE MOVIES(
         id integer PRIMARY KEY,
         movie_name text,
         actor_name text,
         actress_name text,
         director_name text,
         year_of_release text)""")
    print("Movies table is created successfully")
    connection.commit()


def insert_data(connection,list):
    cursor = connection.cursor()
    input_query_sql = """INSERT INTO MOVIES(id, movie_name, actor_name, actress_name, director_name, year_of_release) VALUES(?,?,?,?,?,?)"""
    cursor.executemany(input_query_sql, list)
    connection.commit()
    print("Data inserted successfully")


def retrieve_data(connection, actors_list):
    print("Fetching all the  data with name : {} ".format(actors_list))
    cursor = connection.cursor()
    query = "SELECT * FROM MOVIES WHERE actor_name IN {}".format(actors_list)
    cursor.execute(query)
    print(cursor.fetchall())


def retrieve_all_data(connection):
    print("Fetching all the data...")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM MOVIES')
    print(cursor.fetchall())


def check_and_drop_table_if_exists(connection):
    cursor = connection.cursor()
    cursor.execute(''' SELECT count(name) FROM SQLITE_MASTER WHERE type='table' AND name='MOVIES' ''')
    # if the count is 1, then table exists
    if cursor.fetchone()[0] == 1:
        print("MOVIES table already exists...Dropping the table...")
        cursor.execute(''' DROP TABLE MOVIES''')


def prepare_data():
    tuple1 = (1, 'The God Father', 'Al Pacino', 'Diana Keaton', 'Francis Ford Coppola', 'MARCH 14 1972')
    tuple2 = (2, 'The Irishman', 'Al Pacino', 'Anna Paquin', 'Martin Scorsese', 'SEPTEMBER 27 2019')
    tuple3 = (3, 'Inception', 'Cillian Murphy', 'Marion Cotillard', 'Christopher Nolan', 'JULY 16 2010')
    return [tuple1, tuple2, tuple3]


try:
    conn = create_connection()
    create_table(conn)
    data = prepare_data()
    insert_data(conn, data)
    retrieve_all_data(conn)
    list_of_actors = ('Al Pacino','Cillian Murphy')
    retrieve_data(conn, list_of_actors)
finally:
    conn.close()
