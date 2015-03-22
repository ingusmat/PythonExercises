__author__ = 'matthewburleson'
the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
the_list.insert(0, the_list.pop(3))

the_list.remove([1, 2, 3])

for item in the_list:
  if item not in [1, 2, 3]:
    the_list.remove(item)

the_list.extend(range(4,21))

print(the_list)