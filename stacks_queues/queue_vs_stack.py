"""Implement a MyQueue class which implements a queue using two stacks"""


from stack import Stack
class MyQueue():
    def __init__(self):
        self.s1     = Stack()       # * <-- * <-- * <--
        self.s2     = Stack()

    def enqueue(self, data):
        self.s1.push(data)
        print(self.s1.peek())

    def bad_dequeue(self):
        """ This will push and pop the whole of stack twice every time we want to do a dequeue"""
        while self.s1.head:
            temp = self.s1.pop()
            print(temp)
            self.s2.push(temp)
        popped_data = self.s2.pop()
        while self.s2.head:
            self.s1.push(self.s2.pop())

        return popped_data

    def good_dequeue(self):
        """We can be a bit lazy-> swap the stacks only when it is necessary"""
        if self.s2.is_empty():
            # if s2 is empty push the data into the s2 stack only then,  not other wise 
            while self.s1.peek():
                self.s2.push(self.s1.pop())
        # other wise just pop
        return self.s2.pop()
        # we save time by not pushing values back to s1, for every pop() operation 

if __name__ == "__main__":
    test_array = [23, 22, 2, 99, 98, 6]
    q = MyQueue()
    print(test_array, " will be pushed to the stack")
    for element in test_array:
        print("pushing ...", element)
        q.enqueue(element)
    print(q.good_dequeue())
    print(q.good_dequeue())
