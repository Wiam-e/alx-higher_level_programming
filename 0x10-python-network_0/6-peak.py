#!/usr/bin/python3
"""A script for finding peak in list of ints, interview prep
"""

def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_i = None
    for element in list_of_integers:
        if max_i is None or max_i < element:
            max_i = element
    return max_i
