__author__ = 'matthewburleson'

import random

def nchoices(iterable, number_of_items):
    my_list = []
    try:
        for i in range(0, number_of_items):
            my_list.append(random.choice(iterable))
    except:
        return None

    return my_list

print(nchoices("yesterday", 4))
print(nchoices((1,2,3,4,5,6,7), 4))
print(nchoices(list('sdkfgjhlgkahga'), 4))
print(nchoices({"a": "lfkjslk", "b": "something else", "c": 4}, 2))