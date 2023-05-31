#!/usr/bin/python3
"""defineass Square"""


class Square:
    """Rts a square

    Attributes:
        __size size of a side of the square
    """
    def __init__(self, size=0):
        """initia
        Args:
            size (int):  a side of the square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size e an integer")
        else:
            if size < 0:
                raise ValueError("size m be >= 0")
            else:
                self.__size = size
