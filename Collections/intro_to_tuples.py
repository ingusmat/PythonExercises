__author__ = 'matthewburleson'

def stringcases(word):
    try:
        return word.upper(), word.lower(), word.title(), word[::-1]
    except:
        return ()

print(stringcases('capital of utah'))
print(stringcases(12))
print(stringcases(['hi', 'there', 4]))
print(stringcases('gramma'))

def combo(thing1, thing2):
    return_list = []
    for key, value in enumerate(thing1):
        return_list.append((value, thing2[key]))
    return return_list




print(combo(['swallow', 'snake', 'parrot'], 'abc'))