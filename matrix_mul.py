"""
 a function that multiplies 2 matrices:

Read: Matrix multiplication - only Matrix product (two matrices)

Prototype: def matrix_mul(m_a, m_b):

m_a and m_b must be validated with these requirements in this order

m_a and m_b must be an list of lists of integers or floats:

if m_a or m_b is not a list: raise a TypeError exception with the message m_a must be a list or m_b must be a list
if m_a or m_b is not a list of lists: raise a TypeError exception with the message m_a must be a list of lists or m_b must be a list of lists
if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError exception with the message m_a can't be empty or m_b can't be empty
if one element of those list of lists is not an integer or a float: raise a TypeError exception with the message m_a should contain only integers or floats or m_b should contain only integers or floats
if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size): raise a TypeError exception with the message each row of m_a must be of the same size or each row of m_b must be of the same size
If m_a and m_b can’t be multiplied: raise a ValueError exception with the message m_a and m_b can't be multiplied
"""


def matrix_mul(m_a, m_b):
   if not isinstance(m_a, list):
      raise TypeError("m_a must be a list")
   if not isinstance(m_b, list):
      raise TypeError("m_b must be a list")
   if not all(isinstance(m_a[i], list) for i in range(len(m_a))):
      raise TypeError("m_a must be a list of lists")
   if not all(isinstance(m_b[i], list) for i in range(len(m_b))):
      raise TypeError("m_b must be a list of lists")
   if m_a == [] or m_a == [[]]:
      raise ValueError("m_a can't be empty")
   if m_b == [] or m_b == [[]]:
      raise ValueError("m_b can't be empty")
   if not all(isinstance(j, (int, float)) for i in m_a for j in i):
      raise TypeError("m_a should contain only integers or floats")
   if not all(isinstance(j, (int, float)) for i in m_b for j in i):
      raise TypeError("m_b should contain only integers or floats")
   if not all(len(row) == len(m_a[0]) for row in m_a):
      raise TypeError("each row of m_a must be of the same size")
   if not all(len(row) == len(m_b[0]) for row in m_b):
      raise TypeError("each row of m_b must be of the same size")
   if len(m_a[0]) != len(m_b):
      raise ValueError("m_a and m_b can't be multiplied")
   return [[sum(a*b for a, b in zip(X_row, Y_col))
           for Y_col in zip(*m_b)] for X_row in m_a]


print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

