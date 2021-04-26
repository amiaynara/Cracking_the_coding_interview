# There are three types of edits: insertion, deletion or removal
# Find if one string can attained from another using just one edit or none.

# Solution:
def subtract(s1, s2):
    return ''.join(str(abs(ord(c1) - ord(c2))) for c1, c2 in zip(s1, s2))

def check_abnormality(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    i = 0 
    j =0
    abnormalities = 0
    while i< n1  and j<n2:
        if s1[i] != s2[i]:
            abnormalities += 1
            if abnormalitties > 1:
                return False
            i += 1
        i += 1
        j += 1
    return True

def solve(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 == n2:
        # only replacement can work
        res = subtrace(s1, s2)
        if res.count('0') == n1 or res.count('0') == n1 - 1:
            return True
    elif n1 > n2 : 
        if n1 - 1 == n2:        # deletion is required from s1 or insertion is required on s2
            return check_abnormality(s1, s2)
        else:
            return False

    else:
        if n1 - 1 == n2:        # deletion is required from s1 or insertion is required on s2
            return check_abnormality(s2, s1)
        else:
            return False

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    ans = solve(s1, s2)
    print(ans)

