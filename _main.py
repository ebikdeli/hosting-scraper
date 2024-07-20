from hosts.parsvds import operation as parsvds_operation
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
    # Close connection
    close_mysql(config)
    # parsvds_operation.start(3)
    print('OPERATION SUCCESSFUL')
    # time.sleep(5)
