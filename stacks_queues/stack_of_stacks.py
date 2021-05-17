"""Set of stacks should be composed of several stacks and should create a new stack once the previous one is, pop() should return the same values as it would if there were just a single stack)."""


# if the Node type could accept an Stack object it would be best to use each individual stack as a node for stack of stack. It would be easier to pop. In python we are able to do this by using [-1] indexing. Python saves. But in Java probably we would have to use generics <T> to specify the type of Node Class

from stack import Stack

class StackOfStacks():
    def __init__(self, n):
        self.stack_list = []
        self.limit      = n
        self.stack_list.append(Stack())

    def push(self, data):
        if self.stack_list[-1].size == n:
            self.stack_list.append(Stack())
        self.stack_list[-1].push(data)

    def pop(self):
        if self.stack_list[-1].is_empty():
            self.stack_list.pop()

        self.stack_list[-1].pop()

    def pop_at(self, index):
        try: 
            target_stack = self.stack_list[index]
        except:
            print("The index of stack does not exist yet, use 0 indexing")
        target_stack.pop()

if __name__ == "__main__":
    test_array = [23, 22, 2, 99, 98, 6]
    sos = StackOfStacks(3)
    print(test_array, " will be pushed to the stack")
    for element in test_array:
        stack.push(element)
