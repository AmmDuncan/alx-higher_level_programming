#!/usr/bin/python3
"""Define Node Class and SinglyLinkedList"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Initialize Node object"""
        validate_int(data, "data")
        validate_node(next_node, "next_node")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get data

        Returns:
            int: Node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set data attr of node

        Args:
            value (int): int to set as data
        """
        validate_int(value, "data")
        self.__data = value

    @property
    def next_node(self):
        """Get next node

        Returns:
            Node: next Node object in list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set node

        Args:
            value (Node): Node object to set as next node
        """
        validate_node(value, "next_node")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class"""

    def __init__(self):
        """Initialize Singly Linked List"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new value in a sorted linked list

        Args:
            value (int): integer to insert
        """
        prev = None
        cur = self.__head

        while True:
            if cur is None or cur.data > value:
                newNode = Node(value, cur)
                if prev is not None:
                    prev.next_node = newNode
                else:
                    self.__head = newNode
                break
            else:
                prev = cur
                cur = cur.next_node

    def __str__(self):
        """Singly Linked List User Output"""
        cur = self.__head
        str_rep = ""

        while cur is not None:
            str_rep += "{}".format(cur.data)
            if (cur.next_node is not None):
                str_rep += "\n"
            cur = cur.next_node

        return str_rep


def validate_int(val, name):
    """Validate value as integer

    Args:
        val (int): value to check if is int
        name (str): name of value to use in error
    """
    if not isinstance(val, int):
        raise TypeError("{} must be an integer".format(name))


def validate_node(value, name):
    """Validate value as Node

    Args:
        value (Node): value to check if is type Node or Nonde
        name (str): name to use in error message
    """
    if not isinstance(value, Node) and value is not None:
        raise TypeError("{} must be a Node object".format(name))
