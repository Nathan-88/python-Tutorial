ascii_to_leet = {
    'A': '4',
    'E': '3',
    'I': '1',
    'L': '1',
    'O': '0',
    'S': '5',
    'T': '7'
}
s = "Take me to the next level"
leet = ""
#convert strings to uppercase
for c in s:
    c_upper = c.upper()
    #use get() to give a value if key does not exist
    leet += ascii_to_leet.get(c_upper, c_upper)
    
print(leet)