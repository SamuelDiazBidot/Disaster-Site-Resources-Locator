import decimal
from flask import Flask, jsonify, request, json
from flask_cors import CORS

from handler.resources import ResourcesHandler
from handler.requests import RequestHandler
from handler.administrators import AdministratorHandler
from handler.users import UserHandler
from handler.requesters import RequesterHandler
from handler.supplier import SupplierHandler, SupplyHandler
from handler.statistics import StatisticsHandler
from handler.reservations import ReservationsHandler
from handler.purchases import PurchasesHandler

app = Flask(__name__)
CORS(app)

# Class used so that no errors occur when handling numbers with decimal points
class JSonEnc(json.JSONEncoder):

    def default(self, obj):        
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSonEnc, self).default(obj)
        
app.json_encoder = JSonEnc

DELETE = 'DELETE'
PUT = 'PUT'
POST = 'POST'
GET = 'GET'

# Site greetings
@app.route('/')
def greetings():
    return "Welcome to the Disaster Site Resource Locator"

# Register routes
@app.route('/register/administrator', methods=[POST])
def registerAdmin():
    return AdministratorHandler().register(request.json)

@app.route('/register/requester', methods=[POST])
def registerRequester():
    return RequesterHandler().register(request.json)

@app.route('/register/supplier', methods=[POST]) #TODO Test method
def registerSupplier():
    return SupplierHandler().register(request.json)

# User routes
@app.route('/users')
def getAllUsers():
    return UserHandler().getAll()

@app.route('/users/new', methods=[POST]) 
def addUser():
    return UserHandler().add(request.json)

@app.route('/users/<username>', methods=[GET])
def getUserByUsername(username):
    return UserHandler().getByUsername(username)

@app.route('/requesters')
def getAllRequesters():
    return RequesterHandler().getAll()

@app.route('/suppliers')
def getAllSuppliers():
    return SupplierHandler().getAll()

@app.route('/suppliers/<int:id>')
def getSuppliersById(id):
    return SupplierHandler.getSupplierById(id)

@app.route('/requesters/<int:id>')
def getRequesterByID(id):
    return RequesterHandler().getByID(id)

@app.route('/administrators')
def getAllAdministrators():
    return AdministratorHandler().getAll()

@app.route('/administrators/<int:id>')
def getAdministratorByID(id):
    return AdministratorHandler().getByID(id)

# Resources routes
@app.route('/resources', methods=[GET,POST])
def resources():
    if request.method == POST:
        return ResourcesHandler().add(request.json)
    else:
        return ResourcesHandler().getAll()

@app.route('/resources/<int:id>')
def resourcesByID(id):
    return ResourcesHandler().getByID(id)

@app.route('/resources/requests', methods=[GET, POST])
def requested():
    if request.method == POST:
        return RequestHandler().add(request.json)
    else:
        if request.args:
            return RequestHandler().search(request.args)
        else:
            return RequestHandler().getAll()

@app.route('/resources/requests/<int:id>', methods=[GET, DELETE, PUT])
def requestedByID(id):
    if request.method == DELETE:
        return RequestHandler().delete(id)
    elif request.method == PUT:
        return RequestHandler().update(id, request.form)
    else:
        return RequestHandler().getByID(id)

@app.route('/resources/supplies', methods=[GET, POST]) 
def getAllSupply():
    if request.method == POST:
        return SupplyHandler.add(request.json)
    if not request.args:
        return SupplyHandler.getAllSupply()
    else:
        return SupplyHandler.searchSupply(request.args)

@app.route('/resources/supplies/<int:id>', methods=[GET])
def getSupplyById(id):
    return SupplyHandler.getSupplyById(id)

# Reservations and Purchases
@app.route('/reservations', methods = [POST, GET])
def reservations():
    if request.method == POST:
        return ReservationsHandler().add(request.json)
    else:
        return ReservationsHandler().getAll()

@app.route('/reservations/<int:id>', methods = [DELETE, GET])
def reservationsByID(id):
    if request.method == DELETE:
        return ReservationsHandler().delete(id)
    else:
        return ReservationsHandler().getByID(id)

@app.route('/purchases', methods = [POST, GET])
def purchases():
    if request.method == POST:
        return PurchasesHandler().add(request.json)
    else:
        return PurchasesHandler().getAll()

@app.route('/purchases/<int:id>', methods = [DELETE, GET])
def purchasesByID(id):
    if request.method == DELETE:
        return ReservationsHandler().delete(id)
    else:
        return PurchasesHandler().getByID(id)

# Statistics routes
@app.route('/statistics/daily')
def dailyStatistics():
    return StatisticsHandler().getDailyStatistics()

@app.route('/statistics/weekly')
def weeklyStatistics():
    return StatisticsHandler().getWeeklyStatistics()

@app.route('/statistics/district')
def districtStatistics():
    return StatisticsHandler().getDistrictStatistics()