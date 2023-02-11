"""
The join() method in Python is used to concatenate elements of an iterable (such as a list, string, or tuple) with a specified delimiter. It takes the delimiter as an argument and returns a string that is the concatenation of all elements in the iterable, separated by the delimiter.
"""
#example using matrix
lis = [
    ["nae", "John"],
    ["solo", "sarah"]
]

newli = (', '.join(j for i in lis for j in i))
nwlist = [j for i in lis for j in i]
print(newli)
print(nwlist)
print(type(newli))

# example using a dictionary:
dict = {"name": "John", "age": 30, "city": "New York"}
delimiter = ", "
joined_string = delimiter.join("{}: {}".format(k, v) for k, v in dict.items())
print(joined_string)
"""
Note that the join() method can only be called on a string (the delimiter), and not on any other iterable. So, if you want to join elements of a tuple, for example, you'll first have to convert the tuple to a string using a delimiter.
"""
