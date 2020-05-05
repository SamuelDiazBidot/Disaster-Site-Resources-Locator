from flask import jsonify
from handler.utils import to_specified_format, OK
from dao. resources import ResourcesDAO

RESOURCE_FORMAT = ['id', 'type', 'name', 'description']

class ResourcesHandler:
    def getAll(self):
        resources = ResourcesDAO().getAll()
        resources_list = to_specified_format(resources, RESOURCE_FORMAT)
        return jsonify(Reservations = resources_list), OK

    def getByID(self, id):
        resource = ResourcesDAO().getByID(id)
        resource_list = to_specified_format(resource, RESOURCE_FORMAT)
        return jsonify(Reservation = resource_list), OK