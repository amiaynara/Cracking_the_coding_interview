# Given a string write a function to check if it is a permutation of a pallindrome. 

# Solution: 
# A palindrome of even length => Each character count must be even
# A palindrom with odd length => Exactly one character total count must be odd and all others even


# it is important to ask what are the conditions that are required, so ask the interviewer
# - Can the string contain digits, are capital and lower cases not the same.

def solve(s):
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
        if i %2 == 1:
            odd_count += 1
            if odd_count > 1:
                print('False')      #  small improvement
                return 
    if n % 2 == 0 and odd_count == 0:
        print("True")
        return
    if n % 2 == 1 and odd_count == 1:
        print("True")
        return
    print("False")
    return

if __name__ == '__main__':
    s = input()
    solve(s)

# if you think more deeply about the problem you will find that you don't have to keep the count , a light is ON then after even flips of 
# swtich it will still be on  for n as odd -> 0001000 can be made a palindrome. 
