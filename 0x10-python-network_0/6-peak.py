#!/usr/bin/python3
"""A script that finds a  peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_i = None
    for element in list_of_integers:
        if max_i is None or max_i < element:
            max_i = element
    return max_i
