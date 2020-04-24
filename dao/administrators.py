import mariadb

class AdministratorDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python',
        }

        self.conn = mariadb.connect(**config, database = 'disaster_site_resource_locator_db')

    def getAll(self):
        cursor = self.conn.cursor()
        query = "select email, first_name, last_name, phone_number, permission_level from users natural inner join administrators"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result