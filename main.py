from flask import Flask, jsonify, request 

app = Flask(__name__)

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

@app.route('/')
def greetings():
    return "Welcome to the Disaster Site Resource Locator"

@app.route('/resources', methods=['GET', 'POST'])
def getAllResources():
    # Todo POST method
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return jsonify(Resources = resources)
    else:
        return jsonify(Resources = resources)