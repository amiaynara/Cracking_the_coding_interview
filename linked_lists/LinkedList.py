""" this contains linked lists of various types"""
""" Try using inheritence to make all types of linked lists"""

from Node import node

class linked_list():
    def __init__(self):
        self.head    = None
        self.tail    = None
        self.size    = 0

    def insert(self, val):
        new_node     = node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size = 1
            print(f'{val} inserted successfully')
            return 
        self.head.nex    = new_node
        self.head        = new_node
        print(f'{val} inserted successfully')
    
    def delete(self):
        if self.head == None:
            print("cannot delete from an empty linked list")
            return
        if self.head == self.tail: 
            print("last element of the linked list deleted")
            self.tail = None
            self.head = None
            return 
        traverser = self.tail
        while traverser:
            if traverser.nex == self.head:
                self.head = traverser
                traverser.nex = None
                print('Removed')
            traverser = traverser.nex
    def delete_first(self):
        if self.head == None:
            print('Empty linked list')
            return 
        if self.head == self.tail :
            self.head = None
            self.tail = None
            return 
        new_tail = self.tail.nex
        self.tail.nex = None
        self.tail = new_tail
        
    def search(self, index= None, value=None):
        if index != None and value==None:
            traverser = self.tail
            prev = None
            for i in range(index ):
                try:
                    prev = traverser
                    traverser = traverser.nex
                except:
                    return False
            return prev
        if index == None and value != None:
            traverser = self.tail
            prev = None
            while traverser:
                if traverser.value == value:
                    print('return prev node')
                    return prev
                prev = traverser
                traverser = traverser.nex
            return False

    def delete_at(self, index):
        prev = self.search(index = index)
        if prev == False:
            # no such element with the inex
            print('No such inddex')
            return
        self.delete_node(prev)

    def delete_data(self, value):
        prev = self.search(value=value)
        if prev == False:
            print('No such value present in the linked list')
            return
        self.delete_node(prev)
    
    def delete_node(self, prev):
        if prev == None:
            self.delete_first()
            return 
        if prev.nex == self.head:
            self.delete()
            return
        if prev == False:
            print('the item is not present, please check the input')
            return 
        prev.nex = prev.nex.nex

    def peek(self):
        if self.head == None:
            print("The linked list is  empty")
            return
        print(self.head.value)

    def show(self):
        if self.head == None:
            print('Empty Linked List, nothing to show')
            return 
        traverser = self.tail
        while traverser: 
            print(traverser.value, end = " ")
            traverser = traverser.nex

            
