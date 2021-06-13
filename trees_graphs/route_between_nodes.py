"""4.1  Given a directed graph, design an algorithm to find out whether there is a route between two nodes. """

# Solution
# finding path => bfs

from graph_representation import create_adj_list, take_input

# given a graph and two nodes
def bfs(node):
    q = []
    q.append(node)
    visited = []
    while len(q) > 0:
        curr = q.pop(0)
        for neighbour in graph[curr]:
            if neighbour not in visited: 
                q.append(neighbour)
                visited.append(neighbour)
                if neighbour == n2:
                    return True
                print(neighbour)
    return False

m, n, edges = take_input()
n1, n2 = 7, 9
graph = create_adj_list(edges, directed=True)
# solution 1
print(bfs(n1))

# solution 2
# other is just using dfs
# discuss the tradeoff between the two. 

