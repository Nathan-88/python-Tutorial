def addupto(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def addup(n):
    return n * (n+1)/ 2

num = 6
print(addupto(num))
print(addup(num))
