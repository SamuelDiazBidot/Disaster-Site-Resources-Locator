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
        query = 'select reservation_id, reservation_date, reservation_quantity, supply_id, requester_id from reservations where requester_id = ?'
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result

    def add(self, json):
        cursor = self.conn.cursor()
        query = 'insert into reservations (reservation_date, reservation_quantity, supply_id, requester_id) values (?,?,?,?)'
        cursor.execute(query, (json['date'], json['quantity'], json['supply_id'], json['requester_id']))
        reservation_id = cursor.lastrowid
        self.conn.close()
        return reservation_id

    def delete(self, id):
        cursor = self.conn.cursor()
        query = 'delete from reservations where reservation_id=?'
        cursor.execute(query, (id,))
        self.conn.close()
        return