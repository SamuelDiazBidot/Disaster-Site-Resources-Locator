from flask import Flask, jsonify, request 
from flask_cors import CORS

from handler.availableResource import AvailableResourceHandler
from handler.requestedResource import RequestedResourceHandler
from handler.administrator import AdministratorHandler
from handler.requester import RequesterHandler
from handler.supplier import SupplierHandler
from handler.statistics import StatisticsHandler

app = Flask(__name__)
CORS(app)

@app.route('/')
def greetings():
    return "Welcome to the Disaster Site Resource Locator"

@app.route('/register/administrator', methods=['GET'])
def registerAdmin():
    return AdministratorHandler().register(request.json)

@app.route('/register/requester')
def registerRequester():
    return RequesterHandler().register(request.json)

@app.route('/register/supplier')
def registerSupplier():
    return SupplierHandler().register(request.json)

@app.route('/resources/request', methods=['GET', 'POST'])
def requested():
    if request.method == 'POST':
        return RequestedResourceHandler().add(request.json)
    else:
        if request.form:
            return RequestedResourceHandler().getByKeyword(request.form)
        else:
            return RequestedResourceHandler().getAll()

@app.route('/resources/request/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def requestedByID(id):
    if request.method == 'DELETE':
        return RequestedResourceHandler().delete(id)
    elif request.method == 'PUT':
        return RequestedResourceHandler().update(id, request.form)
    else:
        return RequestedResourceHandler().getByID(id)

@app.route('/resources/available', methods=['GET', 'POST'])
def available():
    if request.method == 'POST':
        return AvailableResourceHandler().add(request.json)
    else:
        if request.form:
            return AvailableResourceHandler().getByKeyword(request.form)
        else:
            return AvailableResourceHandler().getAll()

@app.route('/resources/available/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def availableByID(id):
    if request.method == 'DELETE':
        return AvailableResourceHandler().delete(id)
    elif request.method == 'PUT':
        # AvailableResourceHandler().update(id, request.form)
        return AvailableResourceHandler().reserve(id)
    else:
        return AvailableResourceHandler().getByID(id)

@app.route('/statistics/daily')
def dailyStatistics():
    return StatisticsHandler().getDailyStatistics()

@app.route('/statistics/weekly')
def weeklyStatistics():
    return StatisticsHandler().getWeeklyStatistics()

@app.route('/statistics/district')
def districtStatistics():
    return StatisticsHandler().getDistrictStatistics()