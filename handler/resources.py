from flask import jsonify
from handler.utils import to_specified_format, OK, CREATED, BAD_REQUEST
from dao. resources import ResourcesDAO

RESOURCE_FORMAT = ['id', 'type', 'name', 'description']

class ResourcesHandler:
    def add(self, json):
        if json['type'] and json['name'] and json['description']:
            resource = ResourcesDAO().add(json)
            resource_list = to_specified_format(resource, RESOURCE_FORMAT)
            return jsonify(Reservation = resource_list), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST

    def getAll(self):
        resources = ResourcesDAO().getAll()
        resources_list = to_specified_format(resources, RESOURCE_FORMAT)
        return jsonify(Reservations = resources_list), OK

    def getByID(self, id):
        resource = ResourcesDAO().getByID(id)
        resource_list = to_specified_format(resource, RESOURCE_FORMAT)
        return jsonify(Reservation = resource_list), OK