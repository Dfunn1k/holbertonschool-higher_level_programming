#!/usr/bin/python3
"""class square"""


class Square():
    """
    Define a square by:
    private instance attribute(size)
    instation with optional size
    """
    def __init__(self, size=0):
        """
        Args:
            arg1 (int): size of square
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
