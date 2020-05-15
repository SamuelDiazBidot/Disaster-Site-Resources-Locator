import mariadb
from handler.utils import generic_db_connect

class ResourcesDAO:
    def __init__(self):
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

    def add(self, json):
        cursor = self.conn.cursor()
        query = "insert into resources (resource_type, resource_name, resource_description, sold) values (?,?,?,?)"
        cursor.execute(query, (json['type'], json['name'], json['description'], False))
        resource_id = cursor.lastrowid
        query = 'select resource_id, resource_type, resource_name, resource_description from resources where resource_id = ?'
        cursor.execute(query, (resource_id,))
        result = cursor.fetchall()
        self.conn.close()
        return result