__author__ = 'matthewburleson'

def sillycase(string):
    length = len(string)
    half_length = round(length/2)
    first_bit = string[:half_length].lower()
    last_bit = string[half_length:].upper()

    return first_bit + last_bit

print(sillycase('supercalifragilistic'))
