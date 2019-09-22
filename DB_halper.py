
from contextlib import closing
import mysql.connector
from mysql.connector import Error, MySQLConnection
from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
        :param filename: name of the configuration file
        :param section: section of database configuration
        :return: a dictionary of database parameters
        """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

class DB_halper:

    def connect_to_db(self):
        """ Connect to MySQL database """
        db = read_db_config()

        try:
            conn =MySQLConnection(**db)
            if conn.is_connected():
                print('Connected to MySQL database')
            else:
                print('Connection faild.')
        except Error as e:
            print(e)

        finally:
            conn.close()

    def insert_new_to_WishList(self, wishListName, *args_for_db):
        query="INSERT INTO %s(name, price, comment, link) VALUES(%s,%s, %s, %s)"
        args = list()
        for r in args_for_db:
            args.append(r)
        try:
            db = read_db_config()
            conn = MySQLConnection(**db)
            cursor= conn.cursor()
            cursor.execute(query, wishListName, args)
            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def delet_row_in_WishList(self, wishListName, id):
        db_config = read_db_config()

        query = "DELETE FROM %s WHERE id = %s"

        try:
            # connect to the database server
            conn = MySQLConnection(**db_config)

            # execute the query
            cursor = conn.cursor()
            cursor.execute(query, (id))

            # accept the change
            conn.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()

    def update_wish(self, *row):
        # read database configuration
        db_config = read_db_config()
        data=list()
        # prepare query and data
        query = """ UPDATE users
                        SET name = '%s'
                        SET price = %s
                        SET comment = '%s'
                        SET link = '%s'
                       """
        for r in row:
            data= data.append(r)
        try:
            conn = MySQLConnection(**db_config)

            # update book title
            cursor = conn.cursor()
            cursor.execute(query, data)

            # accept the changes
            conn.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()

    # def make_new_WishList(self, name):
    #     query = "CREATE TABLE IF NOT EXISTS %s(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) , price INT , comment  VARCHAR(30) , link  VARCHAR(30))"
    #     try:
    #         db = read_db_config()
    #         conn = MySQLConnection(**db)
    #         cursor = conn.cursor()
    #         cursor.execute(query, name)
    #     except Error as error:
    #         print(error)
    #     finally:
    #         cursor.close()
    #         conn.close()


if __name__ == '__main__':
   dbHalper=DB_halper()
   test_args=('kek', 10, "LOL0", "HTTPS//")
   dbHalper.update_wish(test_args)

