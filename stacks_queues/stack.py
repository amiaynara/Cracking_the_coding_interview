"""Implementation of Stack using Linked list"""
from node import Node
class Stack():
    def __init__(self):
        self.size   = 0
        self.head   = None
        self.tail   = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def push(self, data):
        new_node    = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return 
        new_node.next = self.head
        self.head     = new_node
        self.size    += 1
        return True

    def pop(self):
        if self.is_empty():
            print("Stack cannot be popped")
            return 
        popped_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return 
        return self.head.value

if __name__ == "__main__":
    test_array = [23, 22, 2, 99, 98, 6]
    stack = Stack()
    print(test_array, " will be pushed to the stack")
    for element in test_array:
        stack.push(element)
    print("The element at the head :", stack.peek())

    print("Popping Now...")
    while stack.head:
        value = stack.pop()
        print(value, end=" ")

    print()
    print("LIFO => Last In First Out Demonstrated")




