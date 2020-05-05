import decimal
from flask import Flask, jsonify, request, json
from flask_cors import CORS

from handler.resources import ResourcesHandler
from handler.availableResource import AvailableResourceHandler, resourcesAvailable
from handler.requests import RequestHandler
from handler.administrator import AdministratorHandler
from handler.requesters import RequesterHandler
from handler.supplier import SupplierHandler, SupplyHandler
from handler.statistics import StatisticsHandler
from handler.reservations import ReservationsHandler
from handler.purchases import PurchasesHandler
from handler.utils import ClientCartInfo

app = Flask(__name__)
CORS(app)

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
@app.route('/register/administrator')
def registerAdmin():
    return AdministratorHandler().register(request.json)

@app.route('/register/requester')
def registerRequester():
    return RequesterHandler().register(request.json)

@app.route('/register/supplier')
def registerSupplier():
    return SupplierHandler().register(request.json)

# User routes
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

# Resources routes
@app.route('/resources')
def resources():
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

@app.route('/resources/supplies', methods=[GET])
def getAllSupply():
    if not request.args:
        return SupplyHandler.getAllSupply()
    else:
        return SupplyHandler.searchSupply(request.args)

@app.route('/resources/supplies/<int:id>', methods=[GET])
def getSupplyById(id):
    return SupplyHandler.getSupplyById(id)

#Creo que ya no es necesario pq es lo mismo que supplies ^
# @app.route('/resources/available', methods=[GET, POST])
# def available():
    # if request.method == POST:
        # return AvailableResourceHandler().add(request.json)
    # else:
        # if request.form:            
            # return AvailableResourceHandler().getByKeyword(request.form)
        # else:
            # return AvailableResourceHandler().getAll()

# @app.route('/resources/available/<int:id>', methods=[GET, DELETE, PUT])
# def availableByID(id):
    # if request.method == DELETE:
        # return AvailableResourceHandler().delete(id)
    # elif request.method == PUT:
        # AvailableResourceHandler().update(id, request.form)
        # return AvailableResourceHandler().reserve(id)
    # else:
        # return AvailableResourceHandler().getByID(id)

# @app.route('/resources/details/<int:id>', methods=[GET, DELETE, PUT])
# def getResourceDetails(id):
    # if request.method == DELETE:
        # return AvailableResourceHandler().delete(id)
    # elif request.method == PUT:
        # AvailableResourceHandler().update(id, request.form)
        # return AvailableResourceHandler().reserve(id)
    # else:
        # return AvailableResourceHandler().getByID(id)

# Reservations and Purchases
@app.route('/reservations')
def reservations():
    return ReservationsHandler().getAll()

@app.route('/reservations/<int:id>')
def reservationsByID(id):
    return ReservationsHandler().getByID(id)

@app.route('/purchases')
def purchases():
    return PurchasesHandler().getAll()

@app.route('/purchases/<int:id>')
def purchasesByID(id):
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

# Client cart route
@app.route('/requester/cart')
def get_client_cart():
    return ClientCartInfo(resourcesAvailable).get_current_client_car()