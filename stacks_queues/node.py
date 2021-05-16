"""This is a node class, the basic unit for the stack"""

class Node():
    def __init__(self, value, next=None):
        self.value  = value
        self.next   = next
