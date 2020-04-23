from flask import jsonify
from handler.utils import OK
from dao.statistics import StatisticsDAO

matches = {"matched" : 10}

data = { 
    "Most_Available" : []
    , "Most_Requested" : []
    , "Matches" : matches
}

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
       return  jsonify(San_Juan= data, Bayamon = data, Arecibo = data, Mayaguez = data, Ponce = data, Guayama = data, Humacao = data, Carolina = data), OK
