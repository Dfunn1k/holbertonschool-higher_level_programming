#!/usr/bin/python3
""" in this file, i will create a empty class for square"""


class Square():
    """Define a square"""
    def __init__(self, size):
        """
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """return size"""
        return self.__size
