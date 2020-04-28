import mariadb

from handler.utils import DATABASECONFIG

class RequestDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python'
        }

        self.conn = mariadb.connect(**config, database = 'disaster_site_resource_locator_db')
        # self.conn = mariadb.connect(**DATABASECONFIG)

    def getAll(self):
        cursor = self.conn.cursor()
        query = "select request_id, resource_type, resource_name, resource_description, request_quantity, request_date, sold from requests natural inner join resources"
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = "select request_id, resource_type, resource_name, resource_description, request_quantity, request_date, sold from requests natural inner join resources where request_id=?"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByNameOrDescription(self, keyword):
        keyword = '%' + keyword + '%'
        cursor = self.conn.cursor()
        query = "select request_id, resource_type, resource_name, resource_description, request_quantity, request_date, sold from requests natural inner join resources where resource_description like ? or resource_name like ?"
        cursor.execute(query, (keyword,keyword))
        result = cursor.fetchall()
        self.conn.close()
        return result