# for i in range(0, 100):
#     if i < 10:
#         i = str(i).zfill(2)
#     print("{}".format(i), end="")
#     if i != 99:
#         print(", ", end="")
# print("", end=", ")
for i in range(100):
    if i < 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
