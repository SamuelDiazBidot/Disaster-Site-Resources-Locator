from typing import List
from typing import Dict
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

