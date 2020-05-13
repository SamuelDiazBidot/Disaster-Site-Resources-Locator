from flask import jsonify
from handler.utils import to_specified_format, OK, CREATED, BAD_REQUEST
from dao.reservations import ReservationsDAO

RESERVATION_FORMAT = ['id', 'date', 'quantity', 'supply_id', 'requester_id']

class ReservationsHandler:
    def getAll(self):
        reservations = ReservationsDAO().getAll()
        reservations_list = to_specified_format(reservations, RESERVATION_FORMAT)
        return jsonify(Reservations = reservations_list), OK

    def getByID(self, id):
        reservation = ReservationsDAO().getByID(id)
        reservation_list = to_specified_format(reservation, RESERVATION_FORMAT)
        return jsonify(Reservation = reservation_list), OK

    def add(self, json):
        if json['date'] and json['quantity'] and json['supply_id'] and json['requester_id']:
            reservation_id = ReservationsDAO().add(json)
            reservation = [(reservation_id, json['date'], json['quantity'], json['supply_id'], json['requester_id'])]
            print(reservation)
            reservation_list = to_specified_format(reservation, RESERVATION_FORMAT)
            return jsonify(Reservation = reservation_list), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST