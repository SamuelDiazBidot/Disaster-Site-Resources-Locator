from flask import jsonify
from handler.utils import OK
from dao.statistics import StatisticsDAO

#TODO: make request from data base
matches = {"matched" : 10}

class StatisticsHandler:
    def build_most_used(self, row):
        result = {}
        result['amount'] = row[0]
        result['type'] = row[1]
        return result

    def getDailyStatistics(self):
        top_requests = StatisticsDAO().mostRequestedDaily()
        top_supplied = StatisticsDAO().mostSuppliedDaily()
        top_requests_list = []
        top_supplied_list = []
        for row in top_requests:
            result = self.build_most_used(row)
            top_requests_list.append(result)
        for row in top_supplied:
            result = self.build_most_used(row)
            top_supplied_list.append(result)
        return jsonify(Most_Requested = top_requests_list, Most_Available = top_supplied_list, Matches = matches), OK

    def getWeeklyStatistics(self):
        top_requests = StatisticsDAO().mostRequestedWeekly()
        top_supplied = StatisticsDAO().mostSuppliedWeekly()
        top_requests_list = []
        top_supplied_list = []
        for row in top_requests:
            result = self.build_most_used(row)
            top_requests_list.append(result)
        for row in top_supplied:
            result = self.build_most_used(row)
            top_supplied_list.append(result)
        return jsonify(Most_Requested = top_requests_list, Most_Available = top_supplied_list, Matches = matches), OK

    def getDistrictStatistics(self):
        districts = ["sanjuan", "bayamon", "arecibo", "mayaguez", "ponce", "guayama", "humacao", "carolina"]
        data = []
        for distric in districts:
            top_requested = StatisticsDAO().mostRequestedByDistrict(distric)
            top_supplied = StatisticsDAO().mostSuppliedByDistrict(distric)
            top_requests_list = []
            top_supplied_list = []
            for row in top_requested:
                result = self.build_most_used(row)
                top_requests_list.append(result)
            for row in top_supplied:
                result = self.build_most_used(row)
                top_supplied_list.append(result)
            data.append({"top_requested" : top_requests_list, "top_supplied" : top_supplied_list})
        return  jsonify(San_Juan= data[0], Bayamon = data[1], Arecibo = data[2], Mayaguez = data[3], Ponce = data[4], Guayama = data[5], Humacao = data[6], Carolina = data[7]), OK