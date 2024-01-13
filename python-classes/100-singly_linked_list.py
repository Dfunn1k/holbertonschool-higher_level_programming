#!/usr/bin/python3
""" Its is a module for learn about class in python"""


class Node:
    """A class that define a node of a single linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that define a single linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value, None)

        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head

            while tmp.next_node and (tmp.next_node.data < value):
                tmp = tmp.next_node

            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        list_singly = []
        head = self.__head
        msg = ""

        while head is not None:
            list_singly.append(head.data)
            head = head.next_node

        length = len(list_singly)

        for i in range(length):
            if i == length - 1:
                msg += f'{list_singly[i]}'
            else:
                msg += f'{list_singly[i]}\n'

        return msg
