# Assume you have a method isSubstring which checks if one word is a substring of another. given two strings, s1 andd s2. write code to check if s2 is a rotation of s1 using only one call to isSubstring('waterbottle' is rotation of 'erbottlewat').

# solution:
def isSubstring(s, S):
    """returns if s is a substring of S"""
    """ O(n) """
    # 2 pointer algorithm
    i = 0
    j = 0 
    N = len(S)
    n = len(s)
    if n > N:
        return False
    while i < N:
        j = 0
        while  i<N and j< n and S[i] == s[j]:
            j += 1
            i += 1
        else:
            if j == n:
                return True
                break
        i += 1
    return False


def solve(s1, s2):
    grand_string = s1 + s1 
    if isSubstring(s2, grand_string):
        return True
    else:
        return False

if __name__ == '__main__':
    s1 = input()
    s2 = input()        # rotated string of s2, may be
    print(solve(s1, s2))
