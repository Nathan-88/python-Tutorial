#a function that returns a set of common elements in two sets.
def common_elements(set_1, set_2):
    #new = set_1 ^ set_2 # returns letters in a or b but not both
    #new = set_1 | set_2 # returns letters in a or b or both
    #new = set_1 & set_2 # returns only letters in both a and b
    new = set_1 - set_2 # returns letters in a but not in b
    return(new)


set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
