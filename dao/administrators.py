import mariadb
from handler.utils import generic_db_connect 

class AdministratorDAO:
    def __init__(self):
        self.conn = generic_db_connect()

    def getAll(self):
        cursor = self.conn.cursor()
        query = "select email, first_name, last_name, phone_number, permission_level from users natural inner join administrators"
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def getByID(self, id):
        cursor = self.conn.cursor()
        query = "select email, first_name, last_name, phone_number, permission_level from users natural inner join administrators where administrator_id=?"
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
        query = "insert into administrators (permission_level, user_name) values (?, ?)"
        cursor.execute(query, (json['permission_level'], json['user_name']))
        administrator_id = cursor.lastrowid
        query = "select email, first_name, last_name, phone_number, permission_level from users natural inner join administrators where administrator_id=?"
        cursor.execute(query, (administrator_id,))
        result = cursor.fetchall()
        self.conn.close()
        return result