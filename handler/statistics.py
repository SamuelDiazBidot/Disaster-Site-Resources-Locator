from flask import jsonify
from handler.utils import OK
from dao.statistics import StatisticsDAO

class StatisticsHandler:
    def build_most_used(self, row):
        result = {}
        result['amount'] = row[0]
        result['type'] = row[1]
        return result

    def getDailyStatistics(self):
        dao = StatisticsDAO()
        top_requests = dao.mostRequestedDaily()
        top_supplied = dao.mostSuppliedDaily()
        top_reservations = dao.mostReservedDaily()
        top_requests_list = []
        top_supplied_list = []
        top_reservations_list = []
        for row in top_requests:
            result = self.build_most_used(row)
            top_requests_list.append(result)
        for row in top_supplied:
            result = self.build_most_used(row)
            top_supplied_list.append(result)
        for row in top_reservations:
            result = self.build_most_used(row)
            top_reservations_list.append(result)
        return jsonify(Most_Requested = top_requests_list, Most_Supplied= top_supplied_list, Most_Reserved = top_reservations_list), OK

    def getWeeklyStatistics(self):
        dao = StatisticsDAO()
        top_requests = dao.mostRequestedWeekly()
        top_supplied = dao.mostSuppliedWeekly()
        top_reservations = dao.mostReservedDaily()
        top_requests_list = []
        top_supplied_list = []
        top_reservations_list = []
        for row in top_requests:
            result = self.build_most_used(row)
            top_requests_list.append(result)
        for row in top_supplied:
            result = self.build_most_used(row)
            top_supplied_list.append(result)
        for row in top_reservations:
            result = self.build_most_used(row)
            top_reservations_list.append(result)
        return jsonify(Most_Requested = top_requests_list, Most_Supplied = top_supplied_list, Most_Reserved = top_reservations_list), OK

    def getDistrictStatistics(self):
        districts = ["sanjuan", "bayamon", "arecibo", "mayaguez", "ponce", "guayama", "humacao", "carolina"]
        data = []
        dao = StatisticsDAO()
        for distric in districts:
            top_requested = dao.mostRequestedByDistrict(distric)
            top_supplied = dao.mostSuppliedByDistrict(distric)
            top_reservations= dao.mostReservedByDistrict(distric)
            top_requests_list = []
            top_supplied_list = []
            top_reservations_list = []
            for row in top_requested:
                result = self.build_most_used(row)
                top_requests_list.append(result)
            for row in top_supplied:
                result = self.build_most_used(row)
                top_supplied_list.append(result)
            for row in top_reservations:
                result = self.build_most_used(row)
                top_reservations_list.append(result)
            data.append({"Most_Requested" : top_requests_list, "Most_Supplied" : top_supplied_list, "Most_Reserved" : top_reservations_list})
        return  jsonify(San_Juan= data[0], Bayamon = data[1], Arecibo = data[2], Mayaguez = data[3], Ponce = data[4], Guayama = data[5], Humacao = data[6], Carolina = data[7]), OK