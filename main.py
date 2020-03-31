from flask import Flask, jsonify, request 
from flask_cors import CORS

from handler.availableResource import AvailableResourceHandler, resourcesAvailable
from handler.requestedResource import RequestedResourceHandler
from handler.administrator import AdministratorHandler
from handler.requester import RequesterHandler
from handler.supplier import SupplierHandler
from handler.statistics import StatisticsHandler
from handler.address import AddressHandler
from handler.utils import ClientCartInfo


app = Flask(__name__)
CORS(app)

DELETE = 'DELETE'
PUT = 'PUT'
POST = 'POST'
GET = 'GET'

@app.route('/')
def greetings():
    return "Welcome to the Disaster Site Resource Locator"

@app.route('/register/administrator', methods=[GET])
def registerAdmin():
    return AdministratorHandler().register(request.json)

@app.route('/register/requester')
def registerRequester():
    return RequesterHandler().register(request.json)

@app.route('/register/supplier')
def registerSupplier():
    return SupplierHandler().register(request.json)

@app.route('/resources/request', methods=[GET, POST])
def requested():
    if request.method == POST:
        return RequestedResourceHandler().add(request.json)
    else:
        if request.form:
            return RequestedResourceHandler().getByKeyword(request.form)
        else:
            return RequestedResourceHandler().getAll()

@app.route('/resources/request/<int:id>', methods=[GET, DELETE, PUT])
def requestedByID(id):
    if request.method == DELETE:
        return RequestedResourceHandler().delete(id)
    elif request.method == PUT:
        return RequestedResourceHandler().update(id, request.form)
    else:
        return RequestedResourceHandler().getByID(id)

@app.route('/resources/request/<keyword>')
def requestByKeyword(keyword):
    return RequestedResourceHandler().getSortedByKeyword(keyword)

@app.route('/resources/available', methods=[GET, POST])
def available():
    if request.method == POST:
        return AvailableResourceHandler().add(request.json)
    else:
        if request.form:
            # Tengo duda como funciona esto, si funciona de por si o el route que añadi esta demas
            return AvailableResourceHandler().getByKeyword(request.form)
        else:
            return AvailableResourceHandler().getAll()

# Este es para resources availables, entiendo que no debe incluir los resources si no está available.
@app.route('/resources/available/<int:id>', methods=[GET, DELETE, PUT])
def availableByID(id):
    if request.method == DELETE:
        return AvailableResourceHandler().delete(id)
    elif request.method == PUT:
        # AvailableResourceHandler().update(id, request.form)
        return AvailableResourceHandler().reserve(id)
    else:
        return AvailableResourceHandler().getByID(id)

@app.route('/resources/available/<keyword>')
def availableByKeyWord(keyword):
    return AvailableResourceHandler().getByKeyword(keyword)

# Este busca la info de cualquier resource sin importar su estado.
@app.route('/resources/details/<int:id>')
def getResourceDetails():
    pass


@app.route('/statistics/daily')
def dailyStatistics():
    return StatisticsHandler().getDailyStatistics()

@app.route('/statistics/weekly')
def weeklyStatistics():
    return StatisticsHandler().getWeeklyStatistics()

@app.route('/statistics/district')
def districtStatistics():
    return StatisticsHandler().getDistrictStatistics()


''' Address routes '''
# TODO verificar si los routes se quedan o se quitan
@app.route('/address')
def get_all_addresses():
    return AddressHandler.get_all_addresses()

@app.route('/address/country/<country>')
def get_address_by_country(country):
    return AddressHandler.get_by_country(country)

@app.route('/address/district/<district>')
def get_address_by_district(district):
    return AddressHandler.get_by_distric(district)

@app.route('/address/city/<city>')
def get_address_by_city(city):
    return AddressHandler.get_by_city(city)

@app.route('/address/zipcode/<zipcode>')
def get_address_by_zipcode(zipcode):
    return AddressHandler.get_by_zipcode(zipcode)

@app.route('/address/street/<street>')
def get_address_by_street(street):
    return AddressHandler.get_by_street(street)

@app.route('/address/coord/<coords>')
def get_address_by_coordinates(coords):
    return AddressHandler.get_by_coord(coords)


# Client cart route
@app.route('/requester/cart')
def get_client_cart():
    return ClientCartInfo(resourcesAvailable).get_current_client_car()

# Falta añadir lo de resourcepayment (receipt), cart, etc...