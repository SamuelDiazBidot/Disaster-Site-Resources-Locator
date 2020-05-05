import mariadb

from handler.utils import DATABASECONFIG, generic_db_connect

class RequestDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python'
        }

        self.conn = generic_db_connect()
        

    def getAll(self):
        cursor = self.conn.cursor()
        query = "select request_id, resource_type, resource_name, resource_description, request_quantity, request_date from requests natural inner join resources"
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = "with request_address as (select requester_id, first_name, last_name, phone_number, country,city,street from address join users natural inner join requesters where users.address = address.address_id) select request_id, resource_type, resource_name, resource_description, request_quantity, request_date, first_name, last_name, phone_number, country, city, street from requests natural inner join resources natural inner join request_address where request_id=?"
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByKeyword(self, keyword):
        keyword = '%' + keyword + '%'
        cursor = self.conn.cursor()
        query = "select request_id, resource_type, resource_name, resource_description, request_quantity, request_date from requests natural inner join resources where resource_description like ? or resource_name like ? order by resource_name"
        cursor.execute(query, (keyword,keyword))
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByType(self,resource_type):
        cursor = self.conn.cursor()
        query = "select request_id, resource_type, resource_name, resource_description, request_quantity, request_date from requests natural inner join resources where resource_type=? order by resource_name"
        cursor.execute(query, (resource_type,))
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByTypeOrKeyword(self, resource_type, keyword):
        keyword = '%' + keyword + '%'
        cursor = self.conn.cursor()
        query = "select request_id, resource_type, resource_name, resource_description, request_quantity, request_date from requests natural inner join resources where resource_description like ? or resource_name like ? or resource_type=? order by resource_name"
        cursor.execute(query, (keyword, keyword, resource_type))
        result = cursor.fetchall()
        self.conn.close()
        return result