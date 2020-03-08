from flask import Flask, jsonify, request 
from handler.availableResource import AvailableResourceHandler
from handler.requestedResource import RequestedResourceHandler
from handler.administrator import AdministratorHandler
from handler.requester import RequesterHandler
from handler.supplier import SupplierHandler

app = Flask(__name__)

@app.route('/')
def greetings():
    return "Welcome to the Disaster Site Resource Locator"

@app.route('/register/administrator')
def registerAdmin():
    AdministratorHandler().register(request.json)

@app.route('/register/requester')
def registerRequester():
    RequesterHandler().register(request.json)

@app.route('/register/supplier')
def registerSupplier():
    SupplierHandler().register(request.json)

@app.route('/resources/request', methods=['GET', 'POST'])
def requested():
    if request.method == 'POST':
        RequestedResourceHandler().add(request.json)
    else:
        if request.form:
            RequestedResourceHandler().getByKeyword(request.form)
        else:
            RequestedResourceHandler().getAll()

@app.route('/resources/request/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def requestedByID(id):
    if request.method == 'DELETE':
        RequestedResourceHandler().delete(id)
    elif request.method == 'PUT':
        RequestedResourceHandler().update(id, request.form)
    else:
        RequestedResourceHandler().getByID(id)

@app.route('/resources/available', methods=['GET', 'POST'])
def available():
    if request.method == 'POST':
        AvailableResourceHandler().add(request.json)
    else:
        if request.form:
            AvailableResourceHandler().getByKeyword(request.form)
        else:
            AvailableResourceHandler().getAll()

@app.route('/resources/available/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def availableByID(id):
    if request.method == 'DELETE':
        AvailableResourceHandler().delete(id)
    elif request.method == 'PUT':
        # AvailableResourceHandler().update(id, request.form)
        AvailableResourceHandler().reserve(id)
    else:
        AvailableResourceHandler().getByID(id)