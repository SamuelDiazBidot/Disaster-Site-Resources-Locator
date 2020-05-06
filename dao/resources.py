import mariadb
from handler.utils import generic_db_connect

class ResourcesDAO:
    def __init__(self):
        config = {
            'host' : 'localhost' ,
            'user' : 'monty',
            'password' : 'python',
        }

        self.conn = generic_db_connect()

    def getAll(self):
        cursor = self.conn.cursor()
        query = 'select resource_id, resource_type, resource_name, resource_description from resources'
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = 'select resource_id, resource_type, resource_name, resource_description from resources where resource_id = ?'
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result