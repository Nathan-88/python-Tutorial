# d = {
#     'foo': 100,
#     'bar': 25,
#     'baz': 360
# }
# print(d.keys())
# print(d.values())
# print(d.items())
# print(max(k for k, v in d.items()))

# a = [1, 2, 3]
# print(id(a))

# a += [4]
# print(id(a))

# lis =[
#     ["nae", "John"],
#     ["solo", "sarah"]
# ]

# newli = (', '.join(j for i in lis for j in i))
# nwlist = [j for i in lis for j in i]
# print(newli)
# print(nwlist)
# print(type(newli))
# dict = {"name": "John", "age": 30, "city": "New York"}
# delimiter = ", "
# joined_string = delimiter.join("{}: {}".format(k, v) for k, v in dict.items())
# print(joined_string)

# def validate_position(position):
#     if not isinstance(position, tuple) or len(position) != 2:
#         raise TypeError("position must be a tuple of 2 positive integers")
#     if not all(isinstance(i, int) and i > 0 for i in position):
#         raise TypeError("position must be a tuple of 2 positive integers")


# position = (1,22,3)
# validate_position(position)
# print(type(position))
    

# class Square:
#     def __init__(self, side, position):
#         self.side = side
#         self.position = position

#     def shape(self):
        
#         for i in range(self.side):
#             for j in range(self.position[0]):
#                 print("-", end="")
#             for j in range(self.side):
#                 print("#", end="")
#             print("")


# square = Square(3, (3, 0))
# square.shape()


import datetime as dt
mytime = dt.datetime.strptime('0130', '%H%M').time()
mydatetime = dt.datetime.combine(dt.date.today(), mytime)
print(mydatetime)