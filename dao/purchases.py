import mariadb

class PurchasesDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python',
        }

        self.conn = mariadb.connect(**config, database = 'disaster_site_resource_locator_db')

    def getAll(self):
        cursor = self.conn.cursor()
        query = 'select purchase_id, purchase_date, supply_id, requester_id from purchases'
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = 'select purchase_id, purchase_date, supply_id, requester_id from purchases where purchase_id = ?'
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result