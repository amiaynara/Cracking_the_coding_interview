from LinkedList import linked_list

ll = linked_list()


s = [x for x in input().split()]
for i in s:
    ll.insert(i)

head = ll.head
tail = ll.tail
k = 3
traverser = tail 
length = 0
while traverser:
    length += 1
    traverser = traverser.nex
ll.show()
print()
traverser = tail
for i in range(length - k - 1):
    traverser = traverser.nex
print(traverser.value)


# recursive solution
def return_kth(node, k):
    if node == None:
        return 0
    index = return_kth(node.nex, k) + 1
    if index == k:
        print("The kth element from the end is:", node.value)
    return index

return_kth(tail, k)
