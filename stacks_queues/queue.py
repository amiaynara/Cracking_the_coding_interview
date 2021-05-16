"""Linked List Implementation of Queue"""
from node import Node

class Queue():
    def __init__(self):
        self.size   = 0
        self.head   = None
        self.tail   = None


    def is_empty(self):
        if self.head == None: 
            return True
        return False

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return 
        self.head.next = new_node
        self.head = new_node
        self.size     += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot perform dequeue operation ")
            return 
        if self.head == self.tail: 
            print("This was the last element, of the Queue")
            ele = self.tail.value
            self.head = None
            self.tail = None
            return ele
        ele = self.tail.value
        self.tail = self.tail.next 
        return ele 
    
    def peek(self):
        return self.tail.value

if __name__=="__main__":
    test_array = [23, 22, 9, 99 , 33, 34]
    q = Queue()
    print("Enqueuing order")
    print(test_array)
    for ele in test_array:
        q.enqueue(ele)
    print("Peeking... : ", q.peek())
    print("Dequeuing order")
    while q.tail:
        val = q.dequeue()
        print(val, end= " ")

    print("FIFO => Has been demonstrated in the testcode")
