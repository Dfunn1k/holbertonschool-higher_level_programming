#!/usr/bin/python3
"""Class Node"""


class Node:
    """Define a node of a single linked list"""

    def __init__(self, data, next_node=None):
        """Initializating data and next_node.

        Args:
            data (int): value that will be stored in a node.
            next_node (Node): pointer to next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property to retrieve the data.

        Property setter to set and check:
            * Data must be an integer, otherwise raise a TypeError
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Property to retrieve the next_node.

        Property setter to set and check:
            * Next_node can be None or must be a Node
            otherwise raise a TypeError"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""class SIngle linked list"""


class SingleLinkedList:
    """Define a Single Linked List"""

    def __init__(self):
        """Initializating single linked list.

        Args:
            head (node): pointer to head of a SLL.
        """
        self.__head = None

    def sorted_insert(self, value):
        """that inserts a new Node into the correct sorted position in the list

        Args:
            value (int): value that will be stored in a node
            node (node): Instance of the class Node
        """
        node = Node(value, None)
        if self.__head is None:
            self.__head = node
        else:
            current = self.__head
            while current.next_node is not None:
                if node.data > current.next_node.data:
                    current = current.next_node
                else:
                    break
            node.next_node = current.next_node
            current.next_node = node

    def __str__(self):
        """show the single linked list when called.

        Args:
            sll (str): string where it will be stored the SLL

        Return:
            The string(sll)
        """
        sll = ""

        while self.__head:
            sll += str(self.__head.data)
            self.__head = self.__head.next_node
            if self.__head:
                sll += '\n'

        return sll
