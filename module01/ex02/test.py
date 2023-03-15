from vector import Vector

v1 = Vector([[1.], [0.], [1.], [3.], [-1.]])
u1 = Vector([[2.], [1.], [0.], [4.], [5.]])

v2 = Vector([[1.3, 0.1, 1.4, 3.2, -2.]])
u2 = Vector([[2.5, 1., 0.5, 2.8, -3.14]])

# [[1.], [2.]]
# [[1., 2.]]

# dot product between same shape vectors:
print(u1.dot(v1))
print(u2.dot(v2))

# transpose
print(f'Before transpose: {v1}')
v1 = v1.T()
print(f'After transpose: {v1}')

# sum (once v1 has same shape as v2 after transpose)
print(f'Sum: {v1} + {v2} = {v1 + v2}')

# subraction
print(f'Subtraction: {v1} - {v2} = {v1 - v2}')

# multiplication
print(f'Multiplication: {v1} * 3 = {v1 * 3}')
print(f'Multiplication: 3 * {v1} = {3 * v1}')

print(f'Division: {u1} / 3 = {u1 / 3}')

try:
    u3 = 3 / u1
except Exception as e:
    print(f'exception detected: {str(e)}')

# other constructors:
# Should give [[0.], [1.], [2.], [3.]]
w1 = Vector(4)
print(w1)

w2 = Vector((0,8))
w3 = Vector((2, 10))

# should give [[-2.], [-2.] ... ] (__rsub__ != __sub__)
print(f'{w2} - {w3} = {w3.__rsub__(w2)}')

# Should be the same
print(w2)
print(w2.__repr__())