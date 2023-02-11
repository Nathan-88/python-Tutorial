def fiz(m_list = 0):
    he = "Fizz"
    return[he if i % 3 == 0 else i for i in m_list]

list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
re = fiz(list)
print(re)
