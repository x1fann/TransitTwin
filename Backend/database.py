import pymysql
import pymysql.cursors

# 数据库连接配置
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'db': 'my_track_data_1',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_connection():
    """
    创建并返回一个新的数据库连接。
    """
    return pymysql.connect(**db_config)

def fetch_data(query, params):
    """
    执行查询并返回结果。
    :param query: SQL 查询语句
    :param params: 查询参数
    :return: 查询结果
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        connection.close()
