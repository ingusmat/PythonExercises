__author__ = 'matthewburleson'

def members(my_dict, my_list):
    keys_in_list = 0
    for item in my_list:
        if item in my_dict:
            keys_in_list +=1


    return keys_in_list

print(members({'apples': 1, 'bananas': 2, 'coconuts': 3}, ['apples', 'coconuts', 'grapes', 'strawberries']))