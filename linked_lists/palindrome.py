# Implement a function to check if a inked list is a palindrome.

# Solution:

# One method that I have thought is to reverse the linked list and then compare. 

# reversing without using another list.
from LinkedList import linked_list
def reverse(old_ll):
    if ll.head == ll.tail:
        print('Length <=1, already reversed')
        return ll
    curr = ll.tail.nex
    ll.head = ll.tail       # make head point to the old tail
    ll.head.nex = None      # make the and the head element points to null or None
    while curr:
        successor = curr.nex
        curr.nex = ll.tail
        ll.tail = curr
        curr = successor

    return ll

l = [int(x) for x in input().split()]
ll = linked_list()
for e in l:
    ll.insert(e)
ll.show()
print()
ll = reverse(ll)
ll.show()

# reverse using another linked list

def rev(t):
    if t== None:
        return
    rev(t.nex) 
    rev_ll.insert(t.value)
    print('inserting ', t.value)

rev_ll = linked_list()
rev(ll.tail)
print()
ll.show()
print()
rev_ll.show()
t = ll.tail
p = rev_ll.tail
palindrome = True
while t or p:
    if not (t and p):
        palindrome = False
        print('not a palindrom')    
        break
    if t.value != p.value:
        palindrome = False
        print('Not a palindrome')
        break
    t = t.nex
    p = p.nex
print()
if palindrome:
    print(l, "is a palindrome")
