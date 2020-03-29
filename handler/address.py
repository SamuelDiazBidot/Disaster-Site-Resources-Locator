from typing import Union, List, Dict
from flask import jsonify
from handler.utils import OK, CREATED, ACCEPTED, get_sorted_from_list_with_key


registered_addresses = [
    {
        'country': 'Puerto Rico',
        'city': 'Idk',
        'street' : 'La de la esquina',
        'district': 'nine',
        'zipcode': '00123',
        'coordinates': [15.0, -15.5]
    },

    {
        'country': 'Canada',
        'city': 'Maya',
        'street' : 'Donde esta el church',
        'district': 'Somewhere',
        'zipcode': '00321',
        'coordinates': [67.0, -126.5]
    },

    {
        'country': 'Puerto Rico',
        'city': 'Maya',
        'street' : 'Donde esta el church',
        'district': 'Somewhere',
        'zipcode': '00321',
        'coordinates': [112.0, -186.5]
    },

    {
        'country': 'Puerto Rico',
        'city': 'Maya',
        'street' : 'Donde esta el church',
        'district': 'Somewhere',
        'zipcode': '00984',
        'coordinates': [100.0, 100.5]
    }

]


class AddressHandler:

    @staticmethod
    def get_all_addresses():
        return jsonify(Address=registered_addresses), OK

    @staticmethod
    def get_by_country(country: str):
        return jsonify(Address=get_sorted_from_list_with_key(country, registered_addresses, 'country')), OK

    @staticmethod
    def get_by_distric(district: str):
        return jsonify(Address=get_sorted_from_list_with_key(district, registered_addresses, 'district')), OK

    @staticmethod
    def get_by_city(city: str):
        return jsonify(Address=get_sorted_from_list_with_key(city, registered_addresses, 'city')), OK

    @staticmethod
    def get_by_zipcode(zipcode: Union[str, int]):
        return jsonify(Address=get_sorted_from_list_with_key(zipcode, registered_addresses, 'zipcode')), OK

    @staticmethod
    def get_by_street(street: str):
        return jsonify(Address=get_sorted_from_list_with_key(street, registered_addresses, 'street')), OK

    @staticmethod
    def get_by_coord(coords: Union[int, float]):
        return jsonify(Address=get_sorted_from_list_with_key(coords, registered_addresses, 'coordinates')), OK

