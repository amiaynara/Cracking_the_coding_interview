# implement an algorithm to demonstrate that string has all unique characters. 

# Solution:

string = input()
d= {}
i = 0
unique  = True
while i < len(string):
    if string[i] in d:
        print("Not a unique string")
        unique = False
        break
    else:
        d[string[i]] = 1

    i += 1
if unique:
    print("String is unique")
# it can be guarenteed that the loop will break before 128 iterations since a character (ASCII) can have atmost value of 128. 
