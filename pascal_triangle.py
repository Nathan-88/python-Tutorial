"""
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))


# def pascal_triangle(n):
#   if n <= 0:
#     return []
#   for i in range(n):
#       C = 1
#       for j in range(i+1):
#           print(C, end="")
#           if j < i:
#               print(",", end="")
#           C = C * (i - j) // (j + 1)
#       print()
#   return

# n = 5
# pascal_triangle(n)
