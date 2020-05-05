from flask import jsonify
from handler.utils import to_specified_format, OK
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