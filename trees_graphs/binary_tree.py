"""This module implements a complete binary tree, no level is empty except the last level's"""

from node import Node
class CompleteBinaryTree():
    def __init__(self):
        self.root = None

         
    def create_binary_tree(self, lst):
        """From the given list of digits create a binary tree"""
        self.root = self.add(lst, 0)

        
    def add(self,lst, i):
        """Given list the level order traversal of the tree"""
        if i < len(lst): 
            node = Node(lst[i])
            node.left = self.add(lst, 2*i + 1)
            node.right = self.add(lst, 2*i + 2)
            return node
        else:
            return None

    def level_order_traversal(self):
        """prints the level order traversal of the complete binary tree"""
        """BFS for complete binary tree"""
        q = []
        print("Level order traversal: " , end = " ")
        q.append(self.root)
        self._lot(q)

    def _lot(self, q):
        if len(q) > 0:
            curr_node = q.pop(0)        # dequeue
            if curr_node.left != None:
                q.append(curr_node.left)
            if curr_node.right != None:
                q.append(curr_node.right)
            print(curr_node.value, end=" ")
            self._lot(q)
        else:
            print()
            return 
    
    def in_order(self):
        print("In Order : ", end="")
        self.in_order_recur(self.root)
        print()

    def in_order_recur(self, curr):
        """LNR"""
        if curr.left != None: 
            self.in_order_recur(curr.left)
        print(curr.value, end = " ")
        if curr.right  != None: 
            self.in_order_recur(curr.right)

    def pre_order(self):
        """NLR"""
        print("Pre Order : ", end="")
        self.pre_order_recur(self.root)
        print()

    def pre_order_recur(self, curr):
        print(curr.value, end = " " )
        if curr.left != None:
            self.pre_order_recur(curr.left)
        if curr.right != None:
            self.pre_order_recur(curr.right)
    
    def post_order(self):
        print("Post Order: ", end=" ")
        self.post_order_recur(self.root)
        print()

    def post_order_recur(self, curr):
        if curr.left != None:
            self.post_order_recur(curr.left)
        if curr.right != None:
            self.post_order_recur(curr.right)
        print(curr.value, end = " " )

if __name__=="__main__":
    cbt = CompleteBinaryTree()
    level_order_traversal = [2, 3 ,6, 10 , 1 , 4, 5]
    cbt.create_binary_tree(level_order_traversal)
    print(level_order_traversal)
    cbt.level_order_traversal()
    cbt.in_order()
    cbt.post_order()
    cbt.pre_order()
