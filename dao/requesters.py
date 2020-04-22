import mariadb

class RequestersDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python',
        }

        self.conn = mariadb.connect(**config, database = 'disaster_site_resource_locator_db')

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = 'select email, first_name, last_name, phone_number from users natural inner join requesters'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result