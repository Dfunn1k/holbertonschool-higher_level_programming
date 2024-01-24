#!/usr/bin/python3
"""My class Int"""


class MyInt(int):
    """
    A class used to represent an integer with special comparison behavior.

    ...

    Methods
    -------
    __eq__(self, other):
        Returns True if self is not equal to other, False otherwise.
    __ne__(self, other):
        Returns True if self is equal to other, False otherwise.
    """

    def __eq__(self, other):
        """
        Overrides the default implementation of the equality operator.

        Parameters
        ----------
        other : int
            The integer to compare with.

        Returns
        -------
        bool
            True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the default implementation of the inequality operator.

        Parameters
        ----------
        other : int
            The integer to compare with.

        Returns
        -------
        bool
            True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
