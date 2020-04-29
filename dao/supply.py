import mariadb
from handler.utils import DATABASECONFIG, PERSON_FORMAT, DEFAULTDATABASECONFIG, SUPPLYFORMAT

class SupplierDAO:

    @staticmethod
    def connectDB():
        try:
            conn = mariadb.connect(**DATABASECONFIG)
        except:
            conn = mariadb.connect(**DEFAULTDATABASECONFIG)
        return conn
    
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
        query = 'select {}, {}, {}, {}, {}, {} from supplies natural inner join resources'.format(*SUPPLYFORMAT)
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def getById(id):        
        conn = SupplyDAO.connectDB()
        cursor = conn.cursor()                
        query = 'select {}, {}, {}, {}, {}, {} from supplies natural inner join resources where supply_id=?'.format(*SUPPLYFORMAT)                
        cursor.execute(query,(id,))
        result = cursor.fetchall()
        conn.close()
        return result

    # TODO Test method
    @staticmethod
    def getByKeyword(keyword):
        conn = SupplyDAO.connectDB()
        cursor = conn.cursor()
        query = 'select {}, {}, {}, {}, {}, {}, resource_description from (select * from supplies natural inner join resources) as res where res.resource_description like \"%{}%\"'.format(*SUPPLYFORMAT, keyword)
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
        