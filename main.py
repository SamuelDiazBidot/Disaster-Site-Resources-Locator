import decimal
from flask import Flask, jsonify, request, json
from flask_cors import CORS

from handler.availableResource import AvailableResourceHandler, resourcesAvailable
from handler.requests import RequestHandler
from handler.administrator import AdministratorHandler
from handler.requesters import RequesterHandler
from handler.supplier import SupplierHandler, SupplyHandler
from handler.statistics import StatisticsHandler
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
@app.route('/resources/request', methods=[GET, POST])
def requested():
    if request.method == POST:
        return RequestHandler().add(request.json)
    else:
        if request.args:
            return RequestHandler().search(request.args)
        else:
            return RequestHandler().getAll()

@app.route('/resources/request/<int:id>', methods=[GET, DELETE, PUT])
def requestedByID(id):
    if request.method == DELETE:
        return RequestHandler().delete(id)
    elif request.method == PUT:
        return RequestHandler().update(id, request.form)
    else:
        return RequestHandler().getByID(id)

@app.route('/resources/supply', methods=[GET])
def getAllSupply():
    return SupplyHandler.getAllSupply()

@app.route('/resources/supply/<int:id>', methods=[GET])
def getSupplyById(id):
    return SupplyHandler.getSupplyById(id)

@app.route('/resources/supply/desc/<keyword>', methods=[GET])
def getSupplyByKeyWordDesc(keyword):
    return SupplyHandler.getSupplyByKeyword(keyword)
    

@app.route('/resources/supply/name<keyword>', methods=[GET])
def getSupplyByNameKey():
    #TODO
    pass

@app.route('/resources/available', methods=[GET, POST])
def available():
    if request.method == POST:
        return AvailableResourceHandler().add(request.json)
    else:
        if request.form:            
            # TODO: Parse the request form and decide to execute by keyword, by type or by keyword and type
            return AvailableResourceHandler().getByKeyword(request.form)
        else:
            return AvailableResourceHandler().getAll()

@app.route('/resources/available/<int:id>', methods=[GET, DELETE, PUT])
def availableByID(id):
    if request.method == DELETE:
        return AvailableResourceHandler().delete(id)
    elif request.method == PUT:
        # AvailableResourceHandler().update(id, request.form)
        return AvailableResourceHandler().reserve(id)
    else:
        return AvailableResourceHandler().getByID(id)

@app.route('/resources/details/<int:id>', methods=[GET, DELETE, PUT])
def getResourceDetails(id):
    if request.method == DELETE:
        return AvailableResourceHandler().delete(id)
    elif request.method == PUT:
        # AvailableResourceHandler().update(id, request.form)
        return AvailableResourceHandler().reserve(id)
    else:
        return AvailableResourceHandler().getByID(id)

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