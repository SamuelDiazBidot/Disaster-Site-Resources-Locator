from flask import jsonify

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
    , "reserved" : False
    },
    { "id" : 1
    , "type" : "baby food"
    , "name" : "gerber baby food"
    , "description": "bannana flavor"
    , "SupplierName" : "Jose Rivera"
    , "location" : "Ponce, PR"
    , "price" : 0.0 
    , "reserved" : True
    }
]

matches = {"matched" : 10}

data = { 
    "Most_Available" : resourcesAvailable
    , "Most_Requested" : resourcesRequested
    , "Matches" : matches
}


class StatisticsHandler:
    def getDailyStatistics(self):
        return jsonify(Most_Requested = resourcesRequested, Most_Available = resourcesAvailable, Matches = matches)

    def getWeeklyStatistics(self):
        return jsonify(Most_Requested = resourcesRequested,Most_Available = resourcesAvailable, Matches = matches)

    def getDistrictStatistics(self):
       return  jsonify(San_Juan= data, Bayamon = data, Arecibo = data, Mayaguez = data, Ponce = data, Guayama = data, Humacao = data, Carolina = data)
