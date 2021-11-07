from typing import Any


class Node:
    def __init__(self, val):
        self.val = val
        self.next = Node


class LinkedList:
    def __init__(self):
        self.head = Node
        self.tail = Node

    def push(self, Node):
        Node.next = self.head
        self.head = Node

    def append(self, Node):
        Node.next = self.tail
        self.tail = Node

    def node(self, p):
        n = self.head
        while n is not None:
            if n == p:
                print(n)
    def insert(self, x, data):
        n = self.head
        while n is not None:
            if n.next == x
                break
            n = n.next
        if n is None:
            print("nie ma takiego wezla")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


lista = LinkedList()


n1 = Node(2)
n2 = Node(1)
n3 = Node(0)

lista.push(n2)
lista.push(n3)

assert lista.head == n3