""" Implementation of a graph"""
""" Bfs is used to find shorted path or check if the path exists"""
""" Dfs is used to traverse all the nodes due to its simplicity"""

from graph_representation import create_adj_list, create_adj_mat, take_input

def dfs(curr):
    visited.append(curr)
    print(curr, 'visited')
    for neighbour in adj_list[curr]: 
        if neighbour not in visited: 
            dfs(neighbour)
def bfs(q):
    curr  = q.pop(0)
    visited.append(curr)
    print(curr)
    for neighbour in adj_list[curr]:
        if neighbour not in q and neighbour not in visited:     # this can be avoided if we know about parent
            q.append(neighbour)
    if len(q) > 0:
        bfs(q)
    else:
        print("Done")

if __name__ == "__main__":
    m, n, edges = take_input()
    adj_list = create_adj_list(edges, directed=True)
    visited = []
    dfs(0)
    q = []
    visited = [0]
    q.insert(0, 0)      # index, value
    bfs(q)


