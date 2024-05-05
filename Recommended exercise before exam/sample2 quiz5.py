# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:21:45 2024

@author: georgex
"""

# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    

    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    letter_ord = ord('a')
    line = []
    final = []
    for h in range(height):
        if h % 2 == 0:
            for w in range(width):
                line.append(chr(letter_ord))
                letter_ord += 1
                if letter_ord > ord('z'):
                    letter_ord = ord('a')
            final.append(line)
            line = []
        else:
            for w in range(width):
                line.append(chr(letter_ord))
                letter_ord += 1
                if letter_ord > ord('z'):
                    letter_ord = ord('a')
            line.reverse()
            final.append(line)
            line = []
    for r in final:
        print(''.join(r))
            


if __name__ == '__main__':
    import doctest
    doctest.testmod()
