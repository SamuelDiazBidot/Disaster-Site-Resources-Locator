import mariadb

from handler.utils import DATABASECONFIG, generic_db_connect
class RequestersDAO:
    def __init__(self):
        self.conn = generic_db_connect()

    def getAll(self):
        cursor = self.conn.cursor()
        query = 'select email, first_name, last_name, phone_number from users natural inner join requesters'
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = 'select email, first_name, last_name, phone_number from users natural inner join requesters where requester_id=?'
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        self.conn.close()
        return result

    def add(self, json):
        cursor = self.conn.cursor()
        query = "insert into address (country, city, street, district, zipcode, longitude, latitude) values (?,?,?,?,?,?,?)"
        cursor.execute(query, (json['country'], json['city'], json['street'], json['district'], json['zipcode'], json['longitude'], json['latitude']))
        address_id = cursor.lastrowid
        query = "insert into users (user_name, email, password, first_name, last_name, dob, phone_number, address) values (?,?,?,?,?,?,?,?)"
        cursor.execute(query, (json['user_name'], json['email'], json['password'], json['first_name'], json['last_name'], json['dob'], json['phone_number'], address_id))
        query = "insert into requesters (balance, user_name) values (?, ?)"
        cursor.execute(query, (4, json['user_name']))
        administrator_id = cursor.lastrowid
        query = 'select email, first_name, last_name, phone_number from users natural inner join requesters where requester_id=?'
        cursor.execute(query, (administrator_id,))
        result = cursor.fetchall()
        self.conn.close()
        return result