# Given a string write a function to check if it is a permutation of a pallindrome. 

# Solution: 
# A palindrome of even length => Each character count must be even
# A palindrom with odd length => Exactly one character total count must be odd and all others even


# it is important to ask what are the conditions that are required, so ask the interviewer
# - Can the string contain digits, are capital and lower cases not the same.

s = input()
# skip all the spaces
# assuming lower case to be same as upper case

s = s.replace(' ', '')
s = s.lower()
d = {}
n = 0
for i, e in enumerate(s):
    if e in d:
        d[e] += 1
    else:
        d[e] = 1
    n += 1

even_count = 0
odd_count  = 0
for i in d.values():
    if i %2 == 0:
        even_count += 1
    else:
        odd_count += 1
if n % 2 == 0:
    if even_count == n:
        print("True")
    else:
        print("False")

else:
    if odd_count == 1:
        print("True")
    else:
        print("False")


