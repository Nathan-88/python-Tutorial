# different ways to print list in Python
mylist = ['python', 'javascript', 'c++', 'java']

#using for loop
"""
for i in range(len(mylist)):
    if i == 1:
        continue
    print(mylist[i], end=" ")
"""
#using * symbol
mylist.sort()
print(*mylist)
print(*mylist, sep=",")

#using join() this only works on lists with str type values
print(' '.join(mylist))
