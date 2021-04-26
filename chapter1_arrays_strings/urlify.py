# Write a method to replace all the spaces with '%20'. 

s = input()
length = len(s.rstrip())

# Method 1 
ans = ''
for i, e in enumerate(s):
    if e == " " and i <length:
        ans += '%20'            # copying is very expensive
    else:
        ans += e
print(ans)

# Method 2

for i, e in enumerate(s):
    if e == " " and i <length:
        print('%20', end="")
    else:
        print(e, end="")
