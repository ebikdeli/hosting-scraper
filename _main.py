from hosts.parsvds import operation as parsvds_operation
from hosts.iranserver import operation as iranserver_operation
from db_connection import connect_mysql, close_mysql
from dotenv import dotenv_values
import time


if __name__ == '__main__':
    # host_name = input('Enter your host name without domain (eg: parsvds): ')
    # print(host_name)
    config = dotenv_values()
    # Connect to mysql db
    connection = connect_mysql(host=config['HOST'],
                                port=config['PORT'],
                                database=config['DATABASE'],
                                user=config['USER'],
                                password=config['PASSWORD'])
    # parsvds_operation.start(connection, 3)
    iranserver_operation.start(connection, 7)
    # Close connection
    if connection:
        close_mysql(connection)
    print('OPERATION SUCCESSFUL')
    # time.sleep(5)
