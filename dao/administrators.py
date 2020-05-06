import mariadb
from handler.utils import generic_db_connect 

class AdministratorDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python',
        }

        self.conn = generic_db_connect()

    def getAll(self):
        cursor = self.conn.cursor()
        query = "select email, first_name, last_name, phone_number, permission_level from users natural inner join administrators"
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = "select email, first_name, last_name, phone_number, permission_level from users natural inner join administrators where administrator_id=?"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result