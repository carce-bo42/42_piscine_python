# ZIP FUNCTION

# SET is aligned but order is random: [(0, 0), (2, 2), (1, 1)] or any combination of the 3 tuples.
# LIST is ordered and aligned: [ (0, 0), (1, 1), (2, 2)]
# TUPLE is ordered and aligned ((0, 0), (1, 1), (2, 2))

number_list_1 = [1, 2, 3]
str_list_1 = ['one', 'two', 'three']

# Two iterables are passed
print(set(zip(number_list_1, str_list_1)))
print(list(zip(number_list_1, str_list_1)))
print(tuple(zip(number_list_1, str_list_1)))

print()

# if zip(a, b) it creates a zip with size = min(len(a), len(b))
number_list_1 = [1, 2, 3, 4]
str_list_1 = ['one', 'two']

print(set(zip(number_list_1, str_list_1)))
print(list(zip(number_list_1, str_list_1)))
print(tuple(zip(number_list_1, str_list_1)))

print()
print()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)

c, v =  zip(*result_list)
print('c =', c)
print('v =', v)

# ENUMERATE FUNCTION

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

for item in enumerate(grocery):
  print(item)

print()

for count, item in enumerate(grocery):
  print(count, item)

print()

# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)

