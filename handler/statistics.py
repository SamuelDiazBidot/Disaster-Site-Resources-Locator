from flask import jsonify
from handler.utils import to_specified_format ,OK
from dao.statistics import StatisticsDAO

AMOUNT_FORMAT = ['amount', 'type']

class StatisticsHandler:
    def getDailyStatistics(self):
        dao = StatisticsDAO()
        top_requests = dao.mostRequestedDaily()
        top_supplied = dao.mostSuppliedDaily()
        top_reservations = dao.mostReservedDaily()
        top_requests_list = to_specified_format(top_requests, AMOUNT_FORMAT)
        top_supplied_list = to_specified_format(top_supplied, AMOUNT_FORMAT)
        top_reservations_list = to_specified_format(top_reservations, AMOUNT_FORMAT)
        return jsonify(Most_Requested = top_requests_list, Most_Supplied= top_supplied_list, Most_Reserved = top_reservations_list), OK

    def getWeeklyStatistics(self):
        dao = StatisticsDAO()
        top_requests = dao.mostRequestedWeekly()
        top_supplied = dao.mostSuppliedWeekly()
        top_reservations = dao.mostReservedDaily()
        top_requests_list = to_specified_format(top_requests, AMOUNT_FORMAT)
        top_supplied_list = to_specified_format(top_supplied, AMOUNT_FORMAT)
        top_reservations_list = to_specified_format(top_reservations, AMOUNT_FORMAT)
        return jsonify(Most_Requested = top_requests_list, Most_Supplied = top_supplied_list, Most_Reserved = top_reservations_list), OK

    def getDistrictStatistics(self):
        districts = ["sanjuan", "bayamon", "arecibo", "mayaguez", "ponce", "guayama", "humacao", "carolina"]
        data = []
        dao = StatisticsDAO()
        for distric in districts:
            top_requested = dao.mostRequestedByDistrict(distric)
            top_supplied = dao.mostSuppliedByDistrict(distric)
            top_reservations= dao.mostReservedByDistrict(distric)
            top_requests_list = to_specified_format(top_requested, AMOUNT_FORMAT)
            top_supplied_list = to_specified_format(top_supplied, AMOUNT_FORMAT)
            top_reservations_list = to_specified_format(top_reservations, AMOUNT_FORMAT)
            data.append({"Most_Requested" : top_requests_list, "Most_Supplied" : top_supplied_list, "Most_Reserved" : top_reservations_list})
        return  jsonify(San_Juan= data[0], Bayamon = data[1], Arecibo = data[2], Mayaguez = data[3], Ponce = data[4], Guayama = data[5], Humacao = data[6], Carolina = data[7]), OK