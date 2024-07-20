import mysql.connector
from mysql.connector import CMySQLConnection
from mysql.connector import Error


def connect_mysql(host:str='localhost', port:int=3306, database:str='hosts_db', user:str='root', password:str='1234') -> CMySQLConnection|None:
    """Connect to mysql server. If connect successful return MySQLConnection, if failed return None

    Args:
        host (str, optional): host name of mysql server. Defaults to 'localhost'.
        port (int, optional): mysql server port. Defaults to 3306.
        database (str, optional): database name. Defaults to 'hosts_db'.
        user (str, optional): user name of connection. Defaults to 'root'.
        password (str, optional): password for the user. Defaults to '1234'.

    Returns:
        CMySQLConnection|None: _description_
    """
    try:
        connection = mysql.connector.connect(host=host,
                                            port=port,
                                            database=database,
                                            user=user,
                                            password=password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None


def close_mysql(connection:CMySQLConnection) -> None:
    """Close an active mysql connection

    Args:
        connection (MySQLConnection)
    """
    try:
        connection.close()
        print('Mysql connection closed successfully')
    except Exception as e:
        print(f'Error while closing mysql connection: {e.__str__()}')
