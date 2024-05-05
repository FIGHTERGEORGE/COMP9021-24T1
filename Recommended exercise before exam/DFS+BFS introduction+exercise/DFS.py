#DFS
#count 1 on chessboard

from random import randint
chessboard = [[randint(0,1) for _ in range(4)] for _ in range(4)]
print(chessboard)

#DFS
stack = list()
visited = list()
output = list()
if chessboard[0][0] == 1:
    output.append((0, 0))
for row in range(len(chessboard)):
    for column in range(len(chessboard[0])):
        i = row
        j = column
        stack.append((i, j))
        while len(stack) != 0:
            vertex = stack.pop()
            y = vertex[0]
            x = vertex[1]
            visited.append((y, x))
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                y_after = dy + y
                x_after = dx + x
                if y_after >= 0 and y_after < len(chessboard) and x_after >=0 and\
                        x_after < len(chessboard[0]):
                    if (y_after, x_after) not in visited and (y_after, x_after) not in stack:
                        stack.append((y_after, x_after))
                        if chessboard[y_after][x_after] == 1 and (y_after, x_after) not in output:
                            output.append((y_after, x_after))
print(f'number of \'1\' in chessboard is {len(output)}')
