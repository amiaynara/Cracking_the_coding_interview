from LinkedList import linked_list
ll = linked_list()

s = [x for x in input().split()]
for val in s:
    ll.insert(val)

ll.delete_at(9)
ll.show()
