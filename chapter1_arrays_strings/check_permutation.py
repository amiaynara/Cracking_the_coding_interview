# Given two strings, write a method to decide if one is a permutation of the other. 

# Question : 2
# Solution :
s1 = input()
s2 = input()
d1 = {chr(c): 0 for c in range(97, 123)}
d2 = {chr(c): 0 for c in range(97, 123)}

if len(s1) == len(s2):
    for c1, c2 in zip(s1, s2):
        if c1 not in d1:
            d1[c1] = 1
        else:
            d1[c1] += 1
        if c2 not in d2:
            d2[c2] = 1
        else:
            d2[c2] += 1 
    permutation = True
    for val in d2.keys():
        if d1[val] == d2[val]:
            pass
        else:
            permutation = False
            break
    if permutation:
        print("Is permutation")
    else:
        print("Not a permutation")
else:
    print("Not a permutation")
