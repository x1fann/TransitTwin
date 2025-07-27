import pymysql
import pymysql.cursors

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'db': 'my_track_data_1',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_connection():
    return pymysql.connect(**db_config)

def fetch_data(query, params):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        connection.close()
