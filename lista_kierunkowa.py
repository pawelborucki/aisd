from typing import Any


class Node:
    def __init__(self, value = None,next=None):
        self.value = value
        self.next = next
    
    
class List_:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def push(self, value):
        new_head = Node(value)
        if(self.head == None):
            self.head = new_head
            self.tail = new_head
        else:
            temp = self.head
            self.head = new_head
            self.head.next = temp
    
    def append(self, value:Any):
        new_tail = Node(value)
        if self.head is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail
    def node(self, at:int):
        temp = self.head
        i = 0
        while (i != at):
            temp = temp.next
            i = i + 1
        return temp
    
    def insert(self, value, after):
        new = Node(value)
        temp = after.next
        after.next = new
        new.next = temp
        
    def pop(self):
        node_del = self.head
        self.head = None
        self.head = node_del.next
        return node_del.value
    
    def remove_last(self):
        temp1 = self.head
        temp2 = self.tail
        while (temp1.next != self.tail):
            temp1 = temp1.next
        temp1.next = None
        self.tail = temp1
        return temp2.value
    
    def remove(self, after):
        temp = after.next
        if(temp == self.tail):
            self.tail = after
        temp = temp.next
        after.next = temp
        
    def __repr__(self):
        x = ''
        temp = self.head
        while(temp is not None):
            x = x + ' -> ' + str(temp.value)
            temp = temp.next
        x = x[4:]
        return x      

    def __len__(self):
        temp = self.head
        list_len = 0
        while(temp is not None):
            list_len += 1
            temp = temp.next
        return list_len
    
    
list_=List_()
assert list_.head == None

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'
print(list_)

list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'
print(list_)

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
print(list_)

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element
print(list_)

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'
print(list_)

second_node = list_.node(at=1)
list_.remove(second_node)
assert str(list_) == '1 -> 5'
print(list_)
print('Dlugosc listy:'+str(len(list_)))