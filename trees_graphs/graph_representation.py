""" A module that provides function for creation of adjacency list and/or adjacency matrix """ """ It takes number of nodes(m) and number of edges (n) and the edges (i,j) pairs=> a list of ordered-pairs as input"""

def create_adj_mat(m, n,edges):
    """Returns a 2d list """
    graph = [[0]*m for i in range(n)]
    for i,j in edges:
        graph[i][j] = 1
        graph[j][i] = 1         # undirected graph
    return graph

def create_adj_list(edges, directed=False):
    """Takes only list of tuples representing each edge. """
    """Returns a dictionary of length m"""
    graph = {}
    for i,j in edges:
        if i not in graph:
            graph[i] = []
        if j not in graph :
            graph[j] = []
        graph[i].append(j)
        if directed == False:
            graph[j].append(i)
    return graph

def take_input():
    m = int(input())        # number of nodes
    n = int(input())        # number of edges 
    edges = []
    for i in range(n):
        i, j = [int(x) for x in input().split()]
        edges.append((i,j))
    return m, n, edges

if __name__ == "__main__":
    m, n, edges = take_input()
    create_adj_mat(m,n,edges)
    create_adj_list(edges)

