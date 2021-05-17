"""Implementation of Stack using Linked list"""
from node import Node
class Stack():
    def __init__(self):
        self.size   = 0
        self.head   = None
        self.tail   = None
        self.min    = None

    def is_empty(self):
        if self.head == None:
            return True
        return False
        
    # * <-- * <-- * <--     orientation of stack
    def push(self, data):
        new_node    = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.min  = data
            new_node.min = data
            return 
        if data < self.head.min:
            new_node.min = data     # if the incoming data is lesser than the current min
        else:
            new_node.min = self.head.min      # if the incoming is greater the already existing min
        new_node.next = self.head
        self.head     = new_node
        self.size    += 1
        if data < self.min:     # update the min
            self.min = data
        return True

    def pop(self):
        if self.is_empty():
            print("Stack cannot be popped")
            return 
        if self.head == self.tail:
            popped    = self.head.value
            self.head = None
            self.tail = None
            self.min  = None
            return popped

        popped_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        # update the the min value if the popped value is the min
        # the problem with this solution is that it makes pop() -> O(n)
        #if popped_value == self.min:
        #    traverser = self.head
        #    self.min = self.head.value
        #    while traverser:
        #        if traverser.value < self.min:
        #            self.min = traverser.value
        #        traverser = traverser.next
        # there fore we look for some other solution
        # we track the min in the Node itself.
        return popped_value

    def peek(self):
        if self.is_empty():
            return 
        return self.head.min

    # Q3.2, implement a min function 
    def min(self):
        if is_empty():
            print("Empty Stack")
            return 
        return self.min
if __name__ == "__main__":
    test_array = [23, 22, 2, 99, 98, 6]
    stack = Stack()
    print(test_array, " will be pushed to the stack")
    for element in test_array:
        stack.push(element)
    print("The element at the head :", stack.peek())
    print("The minimum element is: ", stack.min)
    print("Popping Now...")
    while stack.head:
        value = stack.pop()
        print(value, end=" ")

    print()
    print("LIFO => Last In First Out Demonstrated")




