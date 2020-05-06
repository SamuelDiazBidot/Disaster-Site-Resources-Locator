import mariadb
from handler.utils import generic_db_connect

class ReservationsDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python',
        }

        self.conn = generic_db_connect()

    def getAll(self):
        cursor = self.conn.cursor()
        query = 'select reservation_id, reservation_date, reservation_quantity, supply_id, requester_id from reservations'
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = 'select reservation_id, reservation_date, reservation_quantity, supply_id, requester_id from reservations where reservation_id = ?'
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result