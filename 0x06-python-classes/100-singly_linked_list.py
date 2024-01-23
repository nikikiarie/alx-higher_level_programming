#!/usr/bin/python3
"""Defines classes for singly-linked-list"""

class Node:
    """Node in the list"""

    def __init__(self, data, next_node=None):
        """Initialize a node""""

        Args:
            data (int) : data passed
            next_node (Node): next node
        """
        self.data  = data
        self.next_node = next_node

    @property
    def data(self):
        """get/set node data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get/set node next node"""
        return (self.__next_node)
    
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__next_node = value

class SinglyLinkedList:
    """Singly linkedlsit"""

    def __init__(self):
        """Initialize new list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert node in list

        Args:
            value (Node): node to insert
        """
        
        nnode = Node(value)
        if self.__head is None:
            nnode.next_node = None
            self.__head = nnode
        elif self.__head.data > value:
            nnode.next_value - self.__head
            self.__head = nnode
        else:
            tv = self.__head
            while (tv.next_node is not None and tv.next_node.data < value):
                tv = tv.next_node
            nnode.next_node = tv.next_node
            tv.next_node = nnode

    def __str__(self):
        """Defines print() inlist"""
        values =[]
        tv = self.__head
        while tv is not None:
            values.append(str(tv.data))
            tv = tv.next_node
        return ('\n'.join(values))
