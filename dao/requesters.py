import mariadb

from handler.utils import DATABASECONFIG, generic_db_connect
class RequestersDAO:
    def __init__(self):
        # self.conn = mariadb.connect(**DATABASECONFIG)
        # config = {
        #     'host' : 'localhost',
        #     'user' : 'monty',
        #     'password' : 'python',
        # }

        self.conn = generic_db_connect()

    def getAll(self):
        cursor = self.conn.cursor()
        query = 'select email, first_name, last_name, phone_number from users natural inner join requesters'
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = 'select email, first_name, last_name, phone_number from users natural inner join requesters where requester_id=?'
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result