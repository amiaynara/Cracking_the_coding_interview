# Given a circular linked list, implemnt an algorithm that returns the node at teh beginning of the loop.

# A corrupt linked list in which node's next pointer points to an earlier node, so as to make a loop in the linked list.
# like a whistle in  shape. or a 'P' rotated 90 deg clockwise.
# this will lead to infinite loop while traversing, may be for find the head!!

# Solution:

from LinkedList import linked_list

l = [int(x) for x in input().split()]
ll = linked_list()
for i in l:
    ll.insert(i)

ref_hash = {}
traveller = ll.tail
while traveller:
    ref_hash[traveller] = 1
    traveller = traveller.nex
print(ref_hash)

