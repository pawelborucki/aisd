from typing import Any


class Node:
    value: Any
    next: 'Node'


class LinkedList:
    head: Node
    tail: Node

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value: Any) -> None:
        new_node = Node(value)
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node



list_ = LinkedList()
list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'
