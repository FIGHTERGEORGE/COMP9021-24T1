# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:57:36 2024

@author: georgex

day day up
"""

# COMP9021 24T1 - Rachid Hamadi
# Sample Exam Question 2 Solution


'''
You might find the function bin() useful.
Will be tested with n a strictly positive integer.
'''

import sys


def f(n):
    '''
    >>> f(1)
    1 in binary reads as: 1.
    Only one bit is set to 1 in the binary representation of 1.
    >>> f(2)
    2 in binary reads as: 10.
    Only one bit is set to 1 in the binary representation of 2.
    >>> f(3)
    3 in binary reads as: 11.
    2 bits are set to 1 in the binary representation of 3.
    >>> f(7)
    7 in binary reads as: 111.
    3 bits are set to 1 in the binary representation of 7.
    >>> f(2314)
    2314 in binary reads as: 100100001010.
    4 bits are set to 1 in the binary representation of 2314.
    >>> f(9871)
    9871 in binary reads as: 10011010001111.
    8 bits are set to 1 in the binary representation of 9871.
    '''
    # Insert your code here
    b = bin(n)[2:] # you can also use b = f'{n:b}'
    nbOnes = b.count('1')
    # or calculte nbOnes as follows
    #nbOnes = 0
    #for e in b:
    #    if e == '1':
    #        nbOnes += 1
    print(f'{n} in binary reads as: {b}.')
    if nbOnes == 1:
        print(f'Only one bit is set to 1 in the binary representation of {n}.')
    else:
        print(f'{nbOnes} bits are set to 1 in the binary representation of {n}.')
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()