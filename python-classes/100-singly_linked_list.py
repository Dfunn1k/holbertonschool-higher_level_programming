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
        head = self.__head
        current = head

        if head is None:
            self.__head = new_node
        else:
            if current.next_node is None:
                if new_node.data < current.data:
                    new_node.next_node = current
                    self.__head = new_node
                elif new_node.data > current.data:
                    current.next_node = new_node
            else:
                while current.next_node is not None:
                    if current.data < new_node.data <= current.next_node.data:
                        new_node.next_node = current.next_node
                        current.next_node = new_node
                        break
                    elif new_node.data > current.data and \
                            current.next_node.next_node is None:
                        current.next_node.next_node = new_node
                        # current = current.next_node
                        break
                    elif new_node.data > current.data:
                        current = current.next_node
                    elif new_node.data < current.data:
                        new_node.next_node = current
                        self.__head = new_node
                        break

    def __str__(self):
        list_singly = []
        head = self.__head
        msg = ""
        while head is not None:
            list_singly.append(head.data)
            head = head.next_node

        for node in list_singly:
            if node == list_singly[-1]:
                msg += f'{node}'
            else:
                msg += f'{node}\n'

        return msg
