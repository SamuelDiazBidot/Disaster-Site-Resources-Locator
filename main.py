from flask import Flask, jsonify, request 

resourcesRequested = [
    { "id" : 0
    , "type" : "water bottle"
    , "name" : "Nikini bottles"
    , "description" : "36 water bottle pack"
    , "requesterName" : "Johnny Sins"
    , "location" : "NA"
    },
    { "id" : 1
    , "type" : "baby food"
    , "name" : "gerber baby food"
    , "description": "bannana flavor"
    , "requesterName" : "Jose Rivera"
    , "location" : "Ponce, PR"
    },
    { "id" : 2
    , "type" : "gasoline"
    , "name": "puma gas"
    , "description": "20 liters"
    , "requesterName" : "Miguel Navarro"
    , "location" : "San Juan, PR"
    }
]

resourcesAvailable = [
    { "id" : 0
    , "type" : "water bottle"
    , "name" : "Nikini bottles"
    , "description" : "36 water bottle pack"
    , "SupplierName" : "Johnny Sins"
    , "location" : "NA"
    , "price" : 0.0
    },
    { "id" : 1
    , "type" : "baby food"
    , "name" : "gerber baby food"
    , "description": "bannana flavor"
    , "SupplierName" : "Jose Rivera"
    , "location" : "Ponce, PR"
    , "price" : 0.0 
    },
    { "id" : 2
    , "type" : "gasoline"
    , "name": "puma gas"
    , "description": "20 liters"
    , "supplierName" : "Miguel Navarro"
    , "location" : "San Juan, PR"
    , "price" : 10.0
    }
]

app = Flask(__name__)

@app.route('/')
def greetings():
    return "Welcome to the Disaster Site Resource Locator"

# Route to see and post requests for resources
@app.route('/resources/request', methods=['GET', 'POST'])
def requested():
    # Return the resource request and a 201 Ok response if valid
    if request.method == 'POST':
        return jsonify(Request = resourcesRequested[0]), 201
    # Return all requested resources
    else:
        return jsonify(Requests = resourcesRequested)

# Route to see and post available resources
# Le falta la info de quien esta supliendo y si es una donacion o no
@app.route('/resources/available', methods=['GET', 'POST'])
def available():
    # Return the resource suplied and a 201 Ok response if valid
    if request.method == 'POST':
        return jsonify(Available = resourcesAvailable[0]), 201
    # Return all available resources
    else:
        return jsonify(Available = resourcesAvailable)

# Route to see the available resource with a specific id
@app.route('/resources/available/<int:id>', methods=['GET', 'PUT'])
def availableByID(id):
    # GET info of a specific available resource
    if request.method == 'GET':
        return jsonify(available = resourcesAvailable[0]), 201
    # Reserve or purchase a resource if its not already taken
    elif request.method == 'PUT':
        return jsonify(available = resourcesAvailable[0]), 201


