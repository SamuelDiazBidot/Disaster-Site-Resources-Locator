import mariadb
from handler.utils import generic_db_connect

class PurchasesDAO:
    def __init__(self):
        self.conn = generic_db_connect()

    def getAll(self):
        cursor = self.conn.cursor()
        query = 'select purchase_id, purchase_date, supply_id, requester_id from purchases'
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = 'select purchase_id, purchase_date, supply_id, requester_id from purchases where requester_id = ?'
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result

    def add(self, json):
        cursor = self.conn.cursor()
        query = 'insert into purchases (purchase_date, supply_id, requester_id) values (?,?,?)'
        cursor.execute(query, (json['date'], json['supply_id'], json['requester_id']))
        reservation_id = cursor.lastrowid
        self.conn.close()
        return reservation_id

    def delete(self, id):
        cursor = self.conn.cursor()
        query = 'delete from purchases where purchase_id=?'
        cursor.execute(query, (id,))
        self.conn.close()
        return