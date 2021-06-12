"""This is a node for binary tree"""

class Node():
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def set_left(self, left_child):
        self.left = left_child
        return True

    def set_right(self, right_child):
        self.right = right_child
        return True

    def set_parent(self, parent):
        self.parent = parent
        
