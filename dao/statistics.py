import mariadb
from datetime import date, timedelta

class StatisticsDAO:
    def __init__(self):
        config = {
            'host' : 'localhost',
            'user' : 'monty',
            'password' : 'python'
        }

        self.conn = mariadb.connect(**config, database = 'disaster_site_resource_locator_db')

    def mostRequestedDaily(self):
        today = date.today()
        cursor = self.conn.cursor()
        query = 'select count(resource_type),resource_type from requests natural inner join resources where request_date = ? group by resource_type order by count(resource_type) desc limit 3;'
        cursor.execute(query, (today,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def mostSuppliedDaily(self):
        today = date.today()
        cursor = self.conn.cursor()
        query = 'select count(resource_type),resource_type from supplies natural inner join resources where supply_date = ? group by resource_type order by count(resource_type) desc limit 3;'
        cursor.execute(query, (today,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def mostRequestedWeekly(self):
        today = date.today()
        timeDelta = timedelta(days=7)
        last_week = today - timeDelta 
        cursor = self.conn.cursor()
        query = 'select count(resource_type),resource_type from requests natural inner join resources where request_date > ? and request_date < ? group by resource_type order by count(resource_type) desc limit 3;'
        cursor.execute(query, (last_week, today,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def mostSuppliedWeekly(self):
        today = date.today()
        timeDelta = timedelta(days=7)
        last_week = today - timeDelta 
        cursor = self.conn.cursor()
        query = 'select count(resource_type),resource_type from supplies natural inner join resources where supply_date > ? and supply_date < ? group by resource_type order by count(resource_type) desc limit 3;'
        cursor.execute(query, (last_week, today,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def mostRequestedByDistrict(self, district):
        cursor = self.conn.cursor()
        query = 'with districts as (select user_name, district from users join address on users.address = address.address_id) select count(resource_type), resource_type from districts natural inner join requesters natural inner join requests natural inner join resources where district=? group by resource_type order by count(resource_type) desc'
        cursor.execute(query, (district,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def mostSuppliedByDistrict(self, district):
        cursor = self.conn.cursor()
        query = 'with districts as (select user_name, district from users join address on users.address = address.address_id) select count(resource_type), resource_type from districts natural inner join suppliers natural inner join supplies natural inner join resources where district=? group by resource_type order by count(resource_type) desc'
        cursor.execute(query, (district,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result