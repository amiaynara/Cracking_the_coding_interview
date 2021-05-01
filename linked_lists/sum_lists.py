# You have two numbers represented by a linked list, where each node contains a single digit. The digits are store in reverse order, such that the 1'ss digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. 

# Solution:
from LinkedList import linked_list
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
ll1   = linked_list()
ll2   = linked_list()

for i in l1:
    ll1.insert(i)
for i in l2:
    ll2.insert(i)

ll1.show()
ll2.show()
trav1 = ll1.tail
trav2 = ll2.tail        # they call it head
carry = 0
ll_ans = linked_list()
while bool(trav1) or bool(trav2):
    if bool(trav1):
        num1 = trav1.value
        trav1 = trav1.nex
    else:
        num1 = 0

    if bool(trav2):
        num2 = trav2.value
        trav2 = trav2.nex
    else:
        num2 = 0

    print(bool(trav1), bool(trav2))

    s = num2 + num1
    digit = (s + carry) % 10  
    carry = s // 10
    print(f'{num1} + {num2} = {digit} with carry = {carry}')
    ll_ans.insert(digit)

if carry>0:
    ll_ans.insert(1)
print(f'{ll_ans.show()} that is reverse')

# Follow up : 
# suppose the digits are stored in the forward order
l1 = l1[::-1]
l2 = l2[::-1]
# one solution could be to directly to reverse the linked list and then continue with the above approach
# Problem is reversing the linked list

# I think we can use recursion here
def sum_fun(t1, t2):
    n1 = 0
    n2 = 0
    carry = 0
    if t1 and t2 :
        print(t1.value, t2.value)
        carry = sum_fun(t1.nex, t2.nex) 
    if t1 == None and t2 == None:
        return carry
    n1 = t1.value
    n2 = t2.value
    s = n1 + n2 + carry
    carry = s//10
    ll_ans.insert_tail(s%10)
    return carry

ll2 = linked_list()
ll1 = linked_list()
ll_ans = linked_list()
for i in l1:
    ll1.insert(i)
for i in l2:
    ll2.insert(i)
# below also avoid checking when a particular is terminating, both will terminate at the same time, [same length]
if l1 < l2:
    # padding with zeros for l1 -> l2-l1 times
    for i in range(l2-l1):
        ll1.insert_tail(0)

if l2 < l1:
    # padding with zeros for l1 -> l2-l1 times
    for i in range(l1-l2):
        ll2.insert_tail(0)

carry = sum_fun(ll1.tail, ll2.tail)
if carry:
    ll_ans.insert_tail(carry)

ll_ans.show()
