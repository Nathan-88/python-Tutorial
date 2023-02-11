# student = {}

# for i in range(1, 3):
#     name = input(f"Enter student name {i}: ")
#     score = input(f"Enter student score {i}: ")
#     student[name] = score
# print(f"\n{student}")
# for k, v in student.items():
#     print("{}: {}".format(k, v))

# a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
# print(a.get('friends')[-1].get("name"))
# print(a.get('id'))

# for i in range(10, 2, -2):
#     print(i, end=" ")

class User:
    id = 89
    name = "no name"
    __password = None
    
    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User("john")
print(u.name)
print(User.name)
print(u.is_new)
