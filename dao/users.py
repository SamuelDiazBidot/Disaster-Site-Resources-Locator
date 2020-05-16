import mariadb
from handler.utils import generic_db_connect

class UserDAO:
    def __init__(self):
        # self.conn = generic_db_connect()
        pass

    def getAll(self):
        conn = generic_db_connect()
        cursor = conn.cursor()
        query = 'select user_name, email, first_name, last_name, phone_number from users'
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

    def getByUsername(self, username):
        conn = generic_db_connect()
        cursor = conn.cursor()
        query = 'select user_name, email, first_name, last_name, phone_number from users where user_name=?'
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        conn.close()
        return result

    def add(self, json):
        conn = generic_db_connect()
        cursor = conn.cursor()
        query = "insert into address (country, city, street, district, zipcode, longitude, latitude) values (?,?,?,?,?,?,?)"
        cursor.execute(query, (json['country'], json['city'], json['street'], json['district'], json['zipcode'], json['longitude'], json['latitude']))
        address_id = cursor.lastrowid
        query = "insert into users (user_name, email, password, first_name, last_name, dob, phone_number, address) values (?,?,?,?,?,?,?,?)"
        cursor.execute(query, (json['user_name'], json['email'], json['password'], json['first_name'], json['last_name'], json['dob'], json['phone_number'], address_id))
        conn.close()
        return