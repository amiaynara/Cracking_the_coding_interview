l = [ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5],[3,8], [4,5], [4,9], [7,8], [7,9] ]
list_of_maxes_in_each_smaller_list = map(max, l)
m = max(list_of_maxes_in_each_smaller_list) + 1     # since 0-indexed
n = len(l)

with open('edge_list', 'w') as f:
    f.write(str(m))
    f.write('\n')
    f.write(str(n))
    f.write('\n')
    for i,j in l:
        f.write(str(i) + ' ' + str(j) )
        f.write('\n')
