#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list.

    Args:
        my_list (list): List of integers.
    """
    for integer in my_list:
        print("{:d}".format(integer))
        