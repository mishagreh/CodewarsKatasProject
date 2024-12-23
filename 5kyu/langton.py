# https://www.codewars.com/kata/58e6996019af2cff71000081
#
#
from collections import deque
import pdb
from pprint import pprint


def ant(grid, col, row, n, dir=0):
    gr = grid.copy()
    # dirs = deque([0, 1, 2, 3])
    dirs = [0, 1, 2, 3]
    # breakpoint()
    if dir is not None:
        for i in range(dir):
            # dirs.append(dirs.popleft())
            print(dirs[1:])
            # dirs = dirs[1:] + dirs[0]
            dirs.append(dirs.pop(0))
    for move in range(n):
        if gr[row][col]:
            # dirs.append(dirs.popleft())
            # dirs = dirs[1:].append(dirs[0])
            dirs.append(dirs.pop(0))
        else:
            # dirs.appendleft(dirs.pop())
            # dirs = dirs[-1].append(dirs[1:])
            dirs.insert(0, dirs.pop())
        gr[row][col] = int(not gr[row][col])
        match dirs[0]:
            case 0:
                row -= 1
                if row < 0:
                    row = 0
                    gr.insert(0, [0]*len(gr[0]))
            case 1:
                col += 1
                if col == len(gr[0]):
                    for i in gr:
                        i.append(0)
            case 2:
                row += 1
                if row == len(gr):
                    gr.append([0]*len(gr[0]))
            case 3:
                col -= 1
                if col < 0:
                    col = 0
                    for i in gr:
                        i.insert(0, 0)
    print(list(gr))
    return list(gr)


# ant([[1]], 0, 0, 1, 0)
# expected=[[0,0]])
# ant([[0]], 0, 0, 1, 0)
# expected=[[0,1]])
# ant([[1]], 0, 0, 3, 0)
# expected=[[0,1],[0,1]])
ant([
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
], 1, 1, 20, 2)
