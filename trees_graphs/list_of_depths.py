"""4.3 Given a binary tree, design an agorithm which creates a linked list of all the nodes at each depth."""

# Solution: A level order traversal

class LNode():
    def __init__(self, value, nex=None):
        self.value = value
        self.next  = nex

class TNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        if self.head == None:
            return True
        return False

    def add(self, value):
        node = LNode(value)
        if self.is_empty():
            self.tail  = node
            self.head  = node
            return 
        node.next = self.head
        self.head = node
    def show(self):
        traverser = self.head
        while traverser:
            print(traverser.value)
            traverser = traverser.next
        print("end")


def bfs(node):
    q = []
    q.append(node)
    visited = []
    visited.append(0)
    q.append('*')
    ans = [0, '*']
    lls = []
    l0  = LinkedList()
    l0.add(0)
    lls.append(l0)
    ll  = LinkedList()
    k = 0
    while len(q) > 0:
        curr = q.pop(0)
        if curr == '*' and len(q) == 0:
            break
        if curr == '*':
            q.append('*')
            ll = LinkedList()
            lls.append(ll)
            continue
        for neighbour in graph[curr]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.append(neighbour)
                ll.add(neighbour)
    for ll in lls: 
        ll.show()
from graph_representation import take_input, create_adj_list

m, n, edges = take_input()
graph = create_adj_list(edges)
print(graph)
# given that 0 is the root node
bfs(0)

# second solution 
# mark the level for each of the nodes being travelled. 
def dfs(node, l):
    if l == len(lls):
        l.append(LinkedList())
    visited.append(node)
    lls[l].add(curr)
    # for binary tree the below loop gets converted into just two lines
    # dfs(curr.left, l+1)
    # dfs(curr.right, l+1)
    for neighbour in graph[node]:
        if neighbour is not in visited:
            dfs(neighbour, l  + 1)
lls = []
dfs(0, 1)

# solution 3
# instead of adding children to a queue just visit them at once
# idea is when you are at a level get the children of that level in the list
# next time in the loop just use these children as the parents ..... continue
# a nice approach
l = [] 
curr = [0]
while len(curr) > 0:
    l.append(curr)
    parent = curr
    curr = []
    for p in parent:
        if p.left:
            curr.append(p.left) 
        if p.right: 
            curr.append(p.right)


