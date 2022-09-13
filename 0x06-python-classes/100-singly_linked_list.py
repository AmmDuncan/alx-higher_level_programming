#!/usr/bin/python3
"""Define Node Class"""


class Node:
    """Node class

        Raises:
            TypeError: data must be an integer
            TypeError: must be a Node object
    """

    def __init__(self, data, next_node=None):
        """Initialize Node object

        Args:
            data (int): integer to store as Node data
            next_node (Node, optional): Pointer to next Node in list. Defaults to None.
        """
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
        value (Node): value to check if is type Node
        name (str): name to use in error message
    """
    if not isinstance(value, Node):
        raise TypeError("{} must be a Node object".format(name))
