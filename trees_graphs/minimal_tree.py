"""Given a sorted(increasing order) array with unique integer elements, write an algorithm to create  a binary search tree with minimal height. """

# Solution: inorder traversal always leads to sorted array and minimal height implies a complete a binary tree. 

import random      
import math
from node import Node


n = int(input())  # number of nodes. 
height = int(math.log(n, 2))
a = [int(x) for x in  input().split()]
class bst:
    def __init__(self, ref):
        self.root = None
        self.ref  = ref

    def create_bst(self, l, i =0):
        if i < len(l):
            node = Node(l[i])
            node.left = self.create_bst(l, 2*i + 1) 
            node.right = self.create_bst(l, 2*i + 2) 
            if i == 0:
                self.root = node
            return node
        else:
            return None

    def refactor_tree(self):
        self.in_order(self.root, change=True)
    def iot(self):
        self.in_order(self.root)

    def in_order(self,curr, change=False):
        if curr.left != None:
            self.in_order(curr.left, change)
        if change == True:
            curr.value = self.ref.pop(0)
        else:
            print(curr.value)

        if curr.right != None:
            self.in_order(curr.right, change)
    
b = bst(a)
b.create_bst(a)
print("before: " )
b.iot()
b.refactor_tree()
print("after: ")
b.iot()
