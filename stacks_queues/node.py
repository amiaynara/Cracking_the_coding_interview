"""This is a node class, the basic unit for the stack"""

class Node():
    def __init__(self, value, next=None, min=None):
        self.value  = value
        self.next   = next
        self.min    = min           # used to track the minimum up to that point in stack
