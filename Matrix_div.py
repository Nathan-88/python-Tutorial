"""A function that divides all the elements of the given matrix"""


def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    n = len(matrix[0])
    for row in matrix:
        if len(row) != n:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        rounded_row = []
        for element in row:
            rounded_element = round(element / div, 2)
            rounded_row.append(rounded_element)
        result.append(rounded_row)
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
