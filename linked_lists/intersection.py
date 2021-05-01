# Given two(singly) linked list, determine if the two lists intersect. Return the intersecting node. (nodes must be exact same, not just value).

# Solution:

# Get the lengths
# if tails are different then you don't have intersection at all. Return 'No intersection=> no common node'
# if intersection exists, then chop off the initial nodes from the bigger linked list such that, lengths are the same. 
# now compare one by one, once you find .nex for both same return that nodde. 


# Assuming we have two ll given

def chop(n, ll):
    traverser = ll.tail
    for i in range(n):
        traverser = traverser.nex
    ll.tail = traverser     # make the tail point, this is enough to equalise

def find_intersection(ll1, ll2):
    if ll1.head == ll2.head:
        # intersection exists, my implementation of linked list gives direct acces to the head, don't have to traverse to the end. 
        n1 = 0
        n2 = 0 
        t1 = ll1.tail
        t2 = ll2.tail
        while t1 or t2:
            if t1:
                n1 += 1
                t1 = t1.nex
            if t2:
                n2 += 1
                t2 = t2.nex
        # chop off nodes 
        if n1 > n2:                 # if n1 has more nodes 
            chop(n1 - n2, ll1)      # chop off (n1 - n2) nodes from ll1
        if n2 > n1:
            chop(n2 - n1, ll2)
        t1 = ll1.tail
        t2 = ll2.tail
        while t1 != t2:
            t1 = t1.nex
            t2 = t2.nex
        print('Intersection exists')
        print(t1.value)
    else:
        print('No intersection exists')
