
from contextlib import closing
import mysql.connector
from mysql.connector import Error, MySQLConnection
from configparser import ConfigParser


def test_var_args(farg, *args):
   print("formal arg:", farg)
   for arg in args:
         print("another arg:", arg)

class DB_halper:

    def read_db_config(self, filename='config.ini', section='mysql'):
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

    def connect_to_db(self):
        """ Connect to MySQL database """
        db = DB_halper.read_db_config(self)

        try:
            conn =MySQLConnection(**db)
            if conn.is_connected():
                print('Connected to MySQL database')
            else:
                print('Connection faild.')
        except Error as e:
            print(e)


    def insert_new_to_WishList(self, wishListName, *args_for_db):
        query="INSERT INTO %s(name, price, comment, link) VALUES(%s,%s, %s, %s)"
        args = list()
        args.append(wishListName)
        for r in args_for_db:
            args.append(r)
        try:
            db = DB_halper.read_db_config(self)
            conn = MySQLConnection(**db)
            cursor= conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def delet_row_in_WishList(self, wishListName, id):
        db_config = DB_halper.read_db_config(self)

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

    def select_all_rows(self):
        db_config = DB_halper.read_db_config(self)
        query = "SELECT * FROM users"
        try:
            conn = MySQLConnection(**db_config)
            # update book title
            cursor = conn.cursor()
            cursor.execute(query)
            res = cursor.fetchall()

        except Error as error:
            print(error)

        finally:

            cursor.close()
            conn.close()
            return res

    def update_wish(self, *row):
        # read database configuration
        db_config = DB_halper.read_db_config(self)
        data=list()
        # prepare query and data
        query = """
           UPDATE users
           SET price = %s, comment = %s, link = %s
           WHERE name=%s
        """
        for r in row:
            dataElemet = r
            data.append(dataElemet)
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


if __name__ == '__main__':
   dbHalper=DB_halper()

   test_args=["users","test2", 300, "LOL0", "HTTPS//00"]
   # dbHalper.update_wish(test_args[0], test_args[1], test_args[2], test_args[3])
   dbHalper.insert_new_to_WishList(test_args[0], test_args[1], test_args[2], test_args[3], test_args[4])
   print(dbHalper.select_all_rows())
   # test_var_args(1, "two", 3)


