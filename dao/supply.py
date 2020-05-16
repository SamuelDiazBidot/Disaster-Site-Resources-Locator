import mariadb
from handler.utils import DATABASECONFIG, PERSON_FORMAT, DEFAULTDATABASECONFIG, SUPPLYFORMAT, RESOURCEFORMAT, make_google_map_link, generic_db_connect

class SupplierDAO:

    @staticmethod
    def connectDB():        
        return generic_db_connect()
    
    @staticmethod
    def getAll():
        conn = SupplierDAO.connectDB()
        cursor = conn.cursor()
        query = 'select email, first_name, last_name, phone_number from users natural inner join suppliers'
        cursor.execute(query)      
        result = cursor.fetchall()         
        conn.close()        
        return result

    @staticmethod
    def getById(id):
        conn = SupplierDAO.connectDB()
        cursor = conn.cursor()
        query = 'select {}, {}, {}, {} from users natural inner join suppliers where supplier_id=?'.format(*PERSON_FORMAT)
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def add(json):
        conn = SupplierDAO.connectDB()
        cursor = conn.cursor()
        query = 'insert into address (country, city, street, district, zipcode, longitude, latitude) values (?,?,?,?,?,?,?)'
        cursor.execute(query, (json['country'], json['city'], json['street'], json['district'], json['zipcode'], json['longitude'], json['latitude']))
        address_id = cursor.lastrowid
        query = 'insert into users (user_name, email, password, first_name, last_name, dob, phone_number, address) values (?,?,?,?,?,?,?,?)'
        cursor.execute(query, (json['user_name'], json['email'], json['password'], json['first_name'], json['last_name'], json['dob'], json['phone_number'], address_id))
        query = 'insert into suppliers (company_name, user_name) values (?, ?)'
        cursor.execute(query, (json['company_name'], json['user_name']))
        administrator_id = cursor.lastrowid
        query = 'select email, first_name, last_name, phone_number from users natural inner join suppliers where supplier_id=?'
        cursor.execute(query, (administrator_id,))
        result = cursor.fetchall()
        conn.close()
        return result

class SupplyDAO:

    @staticmethod
    def connectDB():
        try:
            conn = mariadb.connect(**DATABASECONFIG)
        except:
            conn = mariadb.connect(**DEFAULTDATABASECONFIG)
        return conn

    @staticmethod
    def gettAll():
        conn = SupplyDAO.connectDB()
        cursor = conn.cursor()
        query = 'select {}, {}, {}, {}, {}, {} from supplies natural inner join resources'.format(*RESOURCEFORMAT)        
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def getById(id):        
        conn = SupplyDAO.connectDB()
        cursor = conn.cursor()                
        # query = 'select {}, {}, {}, {}, {}, {} from supplies natural inner join resources where supply_id=?'.format(*RESOURCEFORMAT)                
        query = "with supply_address as (select supplier_id, first_name, last_name, phone_number, country, city, street from address join users natural inner join suppliers where users.address = address.address_id) select supply_id, resource_type, resource_name, resource_description, supply_quantity, supply_date, first_name, last_name, phone_number, country, city, street from supplies natural inner join resources natural inner join supply_address where supply_id=?"
        cursor.execute(query,(id,))
        result = cursor.fetchall()
        conn.close()
        return result

    
    
    @staticmethod
    def getByKeyword(keyword):
        conn = SupplyDAO.connectDB()
        cursor = conn.cursor()
        keyword = '%' + keyword + '%'                
        query = 'select {}, {}, {}, {}, {}, {} from supplies natural inner join resources where resource_description like ? or resource_name like ? order by resource_name'.format(*RESOURCEFORMAT)        
        cursor.execute(query, (keyword, keyword))
        result = cursor.fetchall()
        conn.close()
        return result

    
    @staticmethod
    def getByType(res_type):
        conn = SupplyDAO.connectDB()
        cursor = conn.cursor()
        query = 'select {}, {}, {}, {}, {}, {} from supplies natural inner join resources where resource_type=? order by resource_name'.format(*RESOURCEFORMAT)
        cursor.execute(query, (res_type, ))
        result = cursor.fetchall()
        conn.close()
        return result

    
    @staticmethod
    def getByKeywordAndType(res_type, keyword):
        conn = SupplyDAO.connectDB()
        cursor = conn.cursor()
        query = 'select {}, {}, {}, {}, {}, {} from supplies natural inner join resources where resource_description like ? or resource_name like ? or resource_type=? order by resource_name'.format(*RESOURCEFORMAT)
        cursor.execute(query, (keyword, keyword, res_type))
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def add(json):
        conn = generic_db_connect()
        cursor = conn.cursor()
        query = 'insert into resources (resource_type, resource_name, resource_description, sold) values (?,?,?,?)'
        cursor.execute(query, (json['type'], json['name'], json['description'], False))
        resource_id = cursor.lastrowid
        query = 'insert into supplies (supply_quantity, supply_date, resource_id, supplier_id, price) values (?,?,?,?,?)'
        cursor.execute(query, (json['quantity'], json['date'], resource_id, json['supplier_id'], json['price']))
        supplier_id = cursor.lastrowid
        query = 'with supply_address as (select supplier_id, first_name, last_name, phone_number, country, city, street from address join users natural inner join suppliers where users.address = address.address_id) select supply_id, resource_type, resource_name, resource_description, supply_quantity, supply_date, first_name, last_name, phone_number, country, city, street from supplies natural inner join resources natural inner join supply_address where supply_id=?'
        cursor.execute(query, (supplier_id, ))
        result = cursor.fetchall()
        conn.close()
        return result