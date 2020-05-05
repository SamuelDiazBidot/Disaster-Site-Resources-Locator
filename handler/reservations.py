from flask import jsonify
from handler.utils import to_specified_format, OK
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