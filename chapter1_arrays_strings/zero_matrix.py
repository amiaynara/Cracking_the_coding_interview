# an algo such that if an element is 0 in m*n matrix, its entire row and column are set to 0.

# Solution: 
m,n = [int(x) for x in input().split()] # m rows, n columns
a = []
for i in range(m):
    row = [ int(x) for x in input().split()]
    a.append(row)

z_cols = []
z_rows = []

ans = [[0]*n for i in range(m)]

print(ans)
for i in range(m):
    for j in range(n):
        if a[i][j] == 0:
            z_rows.append(i)
            z_cols.append(j)

for i in range(m):
    for j in range(n):
        if not (i in z_cols or j in z_rows): 
            ans[i][j] = a[i][j]

print(ans)
