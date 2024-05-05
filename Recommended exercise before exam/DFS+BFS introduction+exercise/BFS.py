# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:08:34 2024

@author: george
"""

#BFSs
#count 1 in chessboard

from random import randint
chessboard = [[randint(0,1) for _ in range(4)] for _ in range(4)]
print(chessboard)
queue = list()
visited = list()
node_one = list()
if chessboard[0][0] == 1:
    node_one.append((0, 0))
for row in range(len(chessboard)):
    for column in range(len(chessboard[0])):
        i = row
        j = column
        queue.append((i, j))
        visited.append((i, j))
        while len(queue) > 0:
            vertex = queue.pop(0)
            y = vertex[0]
            x = vertex[1]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                y_after = y + dy
                x_after = x + dx
                if y_after >= 0 and x_after >=0 and y_after < len(chessboard) and\
                    x_after < len(chessboard[0]):
                    if (y_after, x_after) not in visited:
                        queue.append((y_after, x_after))
                        visited.append((y_after, x_after))
                        if chessboard[y_after][x_after] == 1:
                            node_one.append((y_after, x_after))
print(f"The number of '1' for the chessboard is {len(node_one)}")