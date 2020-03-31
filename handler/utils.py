from typing import List
from typing import Dict
from flask import jsonify
from copy import deepcopy
import re

''' Status Codes '''

OK = 200
CREATED = 201
ACCEPTED = 202

''' Status Codes '''



def get_from_keyword_sorted_from_list(keyword: str, in_dict_list: List[Dict], key,  reserved: bool = None):
    return_list = []
    keyword = keyword.lower()
    finder = re.compile(keyword)
    for entry in in_dict_list:
        item_name = entry[key].lower()
        if reserved is None:
            if finder.search(item_name):
                return_list.append(entry)
        else:            
            if entry['reserved'] is reserved and finder.search(item_name):
                return_list.append(entry)
    return sorted(return_list, key=lambda return_list: return_list[key], reverse=True)


# TODO Quitarle lo del  sort, no hace nada en este caso, hace sort con el mismo key
def get_sorted_from_list_with_key(keyword: str, in_dict_list: List[Dict], dict_key:str):
    return_list = []
    value_is_number = False

    if keyword is None or keyword == '' or keyword.isspace():
        return in_dict_list

    if not isinstance(keyword, int) and not isinstance(keyword, float) and not isinstance(keyword, str):
        raise ValueError

    if not isinstance(keyword, str) and not isinstance(keyword, list):
        keyword = str(keyword)
        value_is_number = True
  
    keyword = keyword.lower()
    finder = re.compile(keyword)
    
    for entry in in_dict_list:
        entry_value = None
        if value_is_number:
            entry_value = str(entry[dict_key])
        elif isinstance(entry[dict_key], list):
            entry_value = entry[dict_key]
        else:
            entry_value = entry[dict_key].lower()

        if isinstance(entry_value, list):
            new_entry_val = str(entry_value[0])            
            if len(entry_value) == 2:
                new_entry_val = new_entry_val + ',' + str(entry_value[1])
                if finder.fullmatch(new_entry_val):                
                    return_list.append(entry)                    
            else:
                # This part is unverified
                for item in entry_value[1:]:
                    new_entry_val = ','.join(str(item))                                        
            if finder.fullmatch(new_entry_val):                
                return_list.append(entry)
        elif finder.search(entry_value):
            return_list.append(entry)
    
    return return_list



# Class used to represent information of user for the clioent cart for
# the first stage, might change later

class ClientCartInfo:

    from handler.requester import requester
    #from handler.availableResource import resourcesAvailable as res
    from random import Random

    res = None

    chooser = Random()

    def __init__(self, res_list):
        self.res = res_list
        self.current_cart = []
        self.current_client = deepcopy(ClientCartInfo.requester)
        self.current_client.pop('password')
        number_of_res = ClientCartInfo.chooser.randint(0, 100)
        for i in range(number_of_res):
            self.current_cart.append(ClientCartInfo.chooser.choice(res_list))
        self.set_client_cart_info()


    def set_client_cart_info(self):
        self.current_client['want_to_buy'] = self.sort_res_list()
        total_cost_resources = 0.0
        for item in self.current_cart:
            total_cost_resources += item['price']
        self.current_client['resource_cost'] = total_cost_resources

    def sort_res_list(self):
        sorted_res_list = []
        for item in self.current_cart:
            if 'quantity' in item:
                item['quantity'] += 1
            else:
                item['quantity'] = 1
                sorted_res_list.append(item)
        return sorted(sorted_res_list, key=lambda sorted_res_list: sorted_res_list['name'].lower())
                
    def get_current_client_car(self):        
        return jsonify(ClientCart=self.current_client), OK