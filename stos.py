from typing import Any
class Node:
    def __init__(self, value = None , next = None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, element: Any) -> None:
        new = Node(element)
        new.next = self.head
        self.head = new
    
    def pop(self) -> Any:
        temp = self.head
        self.head = None
        self.head = temp.next
        return temp.value
    
    def __len__(self):
        temp = self.head
        x = 0
        while(temp):
            x += 1
            temp = temp.next
        return x
    
    def __repr__(self):
        a = ''
        temp = self.head
        while (temp != None):
            a = a + '\n' + str(temp.value)
            temp = temp.next
        a = a[1:]
        return a
    

stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
print(stack)

top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2
print(stack)