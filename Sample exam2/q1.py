# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:34:42 2024

@author: georgex

day day up
"""

# COMP9021 24T1 - Rachid Hamadi
# Sample Exam 2


def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)               

if __name__ == '__main__':
    import doctest
    doctest.testmod()