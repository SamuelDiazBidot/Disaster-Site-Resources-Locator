import mariadb
from datetime import date, timedelta
from handler.utils import generic_db_connect

class StatisticsDAO:
    def __init__(self):
        self.conn = generic_db_connect()

    def mostRequestedDaily(self):
        today = date.today()
        cursor = self.conn.cursor()
        query = 'select count(resource_type),resource_type from requests natural inner join resources where request_date = ? group by resource_type order by count(resource_type) desc limit 3;'
        cursor.execute(query, (today,))
        result = cursor.fetchall()
        return result

    def mostSuppliedDaily(self):
        today = date.today()
        cursor = self.conn.cursor()
        query = 'select count(resource_type),resource_type from supplies natural inner join resources where supply_date = ? group by resource_type order by count(resource_type) desc limit 3;'
        cursor.execute(query, (today,))
        result = cursor.fetchall()
        return result

    def mostReservedDaily(self):
        today = date.today()
        cursor = self.conn.cursor()
        query = " select count(resource_type), resource_type from reservations natural inner join supplies natural inner join resources where reservation_date=? group by resource_type order by count(resource_type) desc"
        cursor.execute(query, (today,))
        result = cursor.fetchall()
        return result

    def mostRequestedWeekly(self):
        today = date.today()
        timeDelta = timedelta(days=7)
        last_week = today - timeDelta 
        cursor = self.conn.cursor()
        query = 'select count(resource_type),resource_type from requests natural inner join resources where request_date > ? and request_date < ? group by resource_type order by count(resource_type) desc limit 3;'
        cursor.execute(query, (last_week, today,))
        result = cursor.fetchall()
        return result

    def mostSuppliedWeekly(self):
        today = date.today()
        timeDelta = timedelta(days=7)
        last_week = today - timeDelta 
        cursor = self.conn.cursor()
        query = 'select count(resource_type),resource_type from supplies natural inner join resources where supply_date > ? and supply_date < ? group by resource_type order by count(resource_type) desc limit 3;'
        cursor.execute(query, (last_week, today,))
        result = cursor.fetchall()
        return result

    def mostReservedWeekly(self):
        today = date.today()
        timeDelta = timedelta(days=7)
        last_week = today - timeDelta 
        cursor = self.conn.cursor()
        query = " select count(resource_type), resource_type from reservations natural inner join supplies natural inner join resources where reservation_date>? and reservation_date<? group by resource_type order by count(resource_type) desc"
        cursor.execute(query, (last_week, today,))
        result = cursor.fetchall()
        return result

    def mostRequestedByDistrict(self, district):
        cursor = self.conn.cursor()
        query = 'with districts as (select user_name, district from users join address on users.address = address.address_id) select count(resource_type), resource_type from districts natural inner join requesters natural inner join requests natural inner join resources where district=? group by resource_type order by count(resource_type) desc'
        cursor.execute(query, (district,))
        result = cursor.fetchall()
        return result

    def mostSuppliedByDistrict(self, district):
        cursor = self.conn.cursor()
        query = 'with districts as (select user_name, district from users join address on users.address = address.address_id) select count(resource_type), resource_type from districts natural inner join suppliers natural inner join supplies natural inner join resources where district=? group by resource_type order by count(resource_type) desc'
        cursor.execute(query, (district,))
        result = cursor.fetchall()
        return result

    def mostReservedByDistrict(self, district):
        cursor = self.conn.cursor()
        query = "with districts as (select user_name, district from users join address on users.address = address.address_id) select count(resource_type), resource_type, district from reservations natural inner join supplies natural inner join resources natural join districts where district=? group by resource_type order by count(resource_type) desc"
        cursor.execute(query, (district,))
        result = cursor.fetchall()
        return result