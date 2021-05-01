"""
A module that contains the general node class
"""

class node():
    def __init__(self, value, nex=None, prev=None):
        self.value  = value
        self.nex    = nex 
        self.prev   = prev      # This allows this node to be used for doubly linked lists as well

    def set_nex(self, node=None):
        self.next   = node

    def get_value(self):
        return self.value
