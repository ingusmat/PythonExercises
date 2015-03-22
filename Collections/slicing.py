__author__ = 'matthewburleson'

def first_and_last_4(iterable):
  first_4 = iterable[:4]
  last_4 = iterable[:len(iterable)-5:-1]
  last_4.sort()
  if type(iterable) is str:
    return first_4 + last_4
  else:
    first_4.extend(last_4)
    return first_4

print(first_and_last_4(list(range(1,50))))