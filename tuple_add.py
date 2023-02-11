"""
a function that adds 2 tuples.
Prototype: def add_tuple(tuple_a=(), tuple_b=()):
Returns a tuple with 2 integers:
The first element should be the addition of the first element of each argument
The second element should be the addition of the second element of each argument
You are not allowed to import any module
"""
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2] + (0, 0)[len(tuple_a):2]
    tuple_b = tuple_b[:2] + (0, 0)[len(tuple_b):2]
    return tuple(map(sum, zip(tuple_a, tuple_b)))


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
