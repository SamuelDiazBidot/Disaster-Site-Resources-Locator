import mariadb

class RequestDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python'
        }

        self.conn = mariadb.connect(**config, database = 'disaster_site_resource_locator_db')

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = 'select request_id, resource_type, resource_name, resource_description, request_quantity, request_date, sold from requests natural inner join resources'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result