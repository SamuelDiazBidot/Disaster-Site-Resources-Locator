from flask import jsonify
from handler.utils import to_specified_format, OK, CREATED, BAD_REQUEST, NOT_FOUND
from dao.purchases import PurchasesDAO

PURCHASE_FORMAT = ['id', 'date', 'supply_id', 'requester_id']

class PurchasesHandler:
    def getAll(self):
        purchases = PurchasesDAO().getAll()
        purchases_list = to_specified_format(purchases, PURCHASE_FORMAT)
        return jsonify(Purchases = purchases_list), OK

    def getByID(self, id):
        purchase = PurchasesDAO().getByID(id)
        purchase_list = to_specified_format(purchase, PURCHASE_FORMAT)
        return jsonify(Purchases = purchase_list), OK

    def add(self, json):
        if json['date'] and json['supply_id'] and json['requester_id']:
            purchase_id = PurchasesDAO().add(json)
            purchase = [(purchase_id, json['date'], json['supply_id'], json['requester_id'])]
            purchase_list= to_specified_format(purchase, PURCHASE_FORMAT)
            return jsonify(Reservation = purchase_list), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST

    def delete(self, id):
        dao = PurchasesDAO()
        if dao.getByID(id):
            dao.delete(id)
            return jsonify(DeleteStatus = 'OK'), OK
        else:
            return jsonify(Error = 'Part not found'), NOT_FOUND