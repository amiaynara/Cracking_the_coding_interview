# aabcccccaaa -> a2b1c5a3       , It can be noticed that it is also a kind of compression
# if this compression is produces shorter string then return that, else return original string

# Solution:

def solve(s):
    # again there can be only 128 or 256 characters
    n = len(s)
    i = 0 
    ans = ''
    while i < n:
        ans += s[i]
        count = 1
        while True and i < n: 
            if i == n-1  and s[i-1] == s[i]:
                ans += str(count)
                i += 1
                break
            if i == n-1 and s[i-1] != s[i]:
                count = 1
                ans +=  str(1)
                i += 1
                break
            if i < n -1 and  s[i+1] == s[i]:
                count += 1
            else:
                ans += str(count)
                i += 1
                break
            i += 1
    print(ans)  
    if len(ans) < n:
        return ans 
    else: 
        return s


if __name__ == '__main__':
    s = input()
    if len(s) <= 2 :
        print(s)
    else:
        compressed_string = solve(s)
        print(compressed_string)
