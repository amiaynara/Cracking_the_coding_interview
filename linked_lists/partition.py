# creating a partition such that all numbers less than x appear before and all number greater than x appear after x. If x is also there in the  list it should be in the right partition anywhere. 

# Solution: 
from LinkedList import linked_list
l =[ int(x) for x in input().split()]
ll = linked_list()
for element in l:
    ll.insert(element)
ll_small = linked_list()
ll_big   = linked_list()

traverser = ll.tail
x = 5
while traverser:
    if traverser.value >= x:
        ll_big.insert(traverser.value)
    else:
        ll_small.insert(traverser.value)
    traverser = traverser.nex

ll_small.head.nex = ll_big.tail
ll.tail = ll_small.tail             # after making sure that ll_small.tail is not null
ll.head = ll_big.head               # after making sure that ll_head.head is not null -> if so ll.head = ll_small.head

ll.show()


# another shorter method (which is mentioned in the book and I also thought as well) is to create another empty linked list and then start inserting at the head or at the tail. based on the value compared to the 'partitioner'. But then I will have to create another function that inserts at the beginning of the linked list in the definition. 


