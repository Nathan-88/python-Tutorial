# s = "hello john"
# s = s.upper()
# print(s.count('L'))
# print(s.find("O",7))# the 7 indicates that it should search through 7 chars
# print(s.find("O"))
# print(f"{s}")
"""
list = ["Jon", "Ned", 8, 99]
print(*list)
print(*list, sep=",")
"""
a = [3,33,4,55]
a.pop(0)
#pops index from the list
a.insert(0, 30)
#adds to the list,position depends on the index specificied
a.append(50)
#extends the list
a.reverse()
#reverses the list
for i in range(len(a)):
    print(a[i], end="")
    if a[i] != len(a) - 1:
        print(" ", end="")

