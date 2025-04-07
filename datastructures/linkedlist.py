from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list: LinkedList[T] = LinkedList(data_type=data_type)

        for item in sequence:
            linked_list.append(item)

        return linked_list

    def append(self, item: T) -> None:
        #Check if item is data type
        if not(isinstance(item,self.data_type)):
            raise TypeError
        #Instatiate a new node
        new_node: LinkedList.Node = LinkedList.Node(data = item)

        #if empty
        if self.empty:
            self.head = self.tail = new_node
        #if not empty
        else:
            if self.tail:
                self.tail.next = new_node
            new_node.previous = self.tail
        
        self.tail = new_node
        self.count += 1
        

    def prepend(self, item: T) -> None:
        #Check if item is data type
        if not(isinstance(item,self.data_type)):
            raise TypeError
        #Instatiate a new node
        new_node: LinkedList.Node = LinkedList.Node(data = item)

        #if empty
        if self.empty:
            self.head = self.tail = new_node
        #if not empty
        else:
            if self.head:
                self.head.next = new_node
            new_node.previous = self.head
        
        self.head = new_node
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        if self.head and self.head.data == target:
            self.prepend(item)
            return

        travel = self.head

        while travel is not None:
            if travel.data == target:
                break
            travel = travel.next

        if travel is None:
            raise ValueError(f"The target item, {target}, is not in the linked list")

        self.count+=1

    def insert_after(self, target: T, item: T) -> None:
        if self.tail and self.tail.data == target:
            self.prepend(item)
            return

        travel = self.head

        while travel is not None:
            if travel.data == target:
                break
            travel = travel.previous

        if travel is None:
            raise ValueError(f"The target item, {target}, is not in the linked list")

        self.count+=1

    def remove(self, item: T) -> None:
        # if self.empty:
        #     raise ValueError(f"The target item, {item}, is not in the linked list")
        
        # if self.tail and self.tail.data == item:
        #     self.clear

        # travel = self.head

        # while travel is not None:
        #     if travel.data == item:
        #         break
        #     travel = travel.next

        # if travel is None:
        #     raise ValueError(f"The target item, {item}, is not in the linked list")

        # self.count+=1
        raise NotImplementedError


    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        if(self.empty):
            raise IndexError
        data = self.tail.data
        if(self.head is not self.tail):
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.count -= 1
        return data

    def pop_front(self) -> T:
        if(self.empty):
            raise IndexError
        data = self.head.data
        if(self.head is not self.tail):
            self.head = self.head.next
            self.head.previous = None
        else:
            self.tail = self.head = None
        self.count -= 1
        return data

    @property
    def front(self) -> T:
        if self.count:
            return self.head.data
        else:
            raise ValueError('The Linked List is empty')

    @property
    def back(self) -> T:
        if self.count:
            return self.tail.data
        else:
            raise ValueError('The Linked List is empty')

    @property
    def empty(self) -> bool:
        return False if self.count else True

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        travel = self.head
        while travel is not None:
            if travel.data == item:
                return True
            travel = travel.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
