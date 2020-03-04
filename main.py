from flask import Flask, jsonify, request 

resources = [
    { "id" : 0
    , "type" : "water bottle"
    , "name" : "Nikini bottles"
    , "description": "36 water bottle pack"
    },
    { "id" : 1
    , "type" : "baby food"
    , "name" : "gerber baby food"
    , "description": "bannana flavor"
    },
    { "id" : 2
    , "type" : "gasoline"
    , "name": "puma gas"
    , "description": "20 liters"
    }
]

app = Flask(__name__)

@app.route('/')
def greetings():
    return "Welcome to the Disaster Site Resource Locator"

# Route to see and post requests for resources
# Le falta la info del que esta requesting (nombre, localizacion, id)
@app.route('/resources/request', methods=['GET', 'POST'])
def requested():
    # Return the resource request and a 201 Ok response if valid
    if request.method == 'POST':
        return jsonify(Request = resources[0]), 201
    # Return all requested resources
    else:
        return jsonify(Requests = resources)

# Route to see and post available resources
# Le falta la info de quien esta supliendo y si es una donacion o no
@app.route('/resources/available', methods=['GET', 'POST'])
def available():
    # Return the resource suplied and a 201 Ok response if valid
    if request.method == 'POST':
        return jsonify(Available = resources[0]), 201
    # Return all available resources
    else:
        return jsonify(Available = resources)

# Route to see the available resource with a specific id
@app.route('/resources/available/<int:id>', methods=['GET', 'PUT'])
def availableByID(id):
    # GET info of a specific available resource
    if request.method == 'GET':
        return jsonify(available = resources[0]), 201
    # Reserve or purchase a resource if its not already taken
    elif request.method == 'PUT':
        return jsonify(available = resources[0]), 201


