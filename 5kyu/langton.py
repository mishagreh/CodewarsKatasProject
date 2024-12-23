# https://www.codewars.com/kata/58e6996019af2cff71000081
#
#
from collections import deque
import pdb


def ant(grid, col, row, n, dir=0):
    grid = deque(grid)
    d = deque([0, 1, 2, 3], maxlen=4)
    # breakpoint()
    for move in range(n):
        # print(move)
        # try:
        color = grid[col][row]
        if color:
            d.append(d.popleft())
            print(col, row)
            print(grid[col][row])
            grid[col][row] = 0
            print(grid[col][row])
        else:
            d.appendleft(d.pop())
            print(col, row)
            print('bef:', grid[col][row])
            grid[col][row] = 1
            print('aft:', grid[col][row])
        dir = d[0]
        match dir:
            case 0:
                col -= 1
                if col < 0:
                    col = 0
                    grid.appendleft([0]*len(grid[0]))
            case 1:
                row += 1
                if row == len(grid[0]):
                    print('case 1:', grid)
                    for i in grid:
                        i.append(0)
                    print('case 1:', grid)
            case 2:
                col += 1
                if col == len(grid[0]):
                    print('case 2:', grid)
                    grid.append([0]*len(grid[0]))
            case 3:
                row -= 1
                if row < 0:
                    print('case 3:', grid)
                    for i, j in enumerate(grid):
                        grid[i] = [0] + j
    print(grid, col, row, n, dir)
    print(list(grid))
    print('___')
    return list(grid)


ant([[1]], 0, 0, 1, 0)
# expected=[[0,0]])
ant([[0]], 0, 0, 1, 0)
# expected=[[0,1]])
ant([[1]], 0, 0, 3, 0)
# expected=[[0,1],[0,1]])
