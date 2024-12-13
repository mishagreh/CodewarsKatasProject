# https://www.codewars.com/kata/56882731514ec3ec3d000009
import pdb
import numpy as np


def v_check(grid):
    # breakpoint()
    for column in grid:
        for color in ('r', 'y'):
            if column.find(4*color) != -1:
                return color
    return


def h_check(grid):
    # breakpoint()
    grid_h = ['' for i in range(7)]
    # print(grid_h)
    for i, column in enumerate(grid):
        for j, row in enumerate(column):
            grid_h[j] += row

    # print(grid_h)
    for column in grid_h:
        for color in ('r', 'y'):
            if column.find(4*color) != -1:
                return color
    return


def d1_check(grid):
    gr = grid.copy()
    for i, column in enumerate(gr):
        c = column[::-1].zfill(6)
        gr[i] = c[::-1]
    # print(gr)
    # a = np.arange(12).reshape(3, 4)
    # print(a)
    # print(a.diagonal(1))
    # print(a.diagonal(2))
    # for i in range(-1, 3):
    #     print(a.diagonal(i))
    for i, j in enumerate(gr):
        gr[i] = list(j)
        # print(gr)
    b = np.array(gr)
    b = b.reshape(7, 6)
    # print(b)
    diags = []
    for i in range(-6, 6):
        # print(b.diagonal(i))
        diags.append(b.diagonal(i).tolist())
    di = []
    for i in diags:
        di.append(''.join(i))
    #     print(i)
    # print(di)
    # diags = diags.tolist()
    for column in di[3:9]:
        for color in ('r', 'y'):
            if column.find(4*color) != -1:
                return color
    return


def d2_check(grid):
    gr = grid.copy()
    for i, column in enumerate(gr):
        c = column[::-1].zfill(6)
        gr[i] = c[::-1]
    # print(gr)
    # a = np.arange(12).reshape(3, 4)
    # print(a)
    # for i in range(-1, 3):
    #     print(np.flipud(a).diagonal(i))
    for i, j in enumerate(gr):
        gr[i] = list(j)
        # print(gr)
    b = np.array(gr)
    b = b.reshape(7, 6)
    # print(b)
    diags = []
    for i in range(-6, 6):
        # print(np.flipud(b).diagonal(i))
        diags.append(np.flipud(b).diagonal(i).tolist())
    di = []
    for i in diags:
        di.append(''.join(i))
        # print(i)
    # print(di)
    for column in di[3:9]:
        for color in ('r', 'y'):
            if column.find(4*color) != -1:
                return color
    return


def who_is_winner(moves):
    grid = ['' for i in range(7)]
    moves = list(map(lambda i: (i[0], 'y' if i[2] == 'Y' else 'r'), moves))
    # print(moves)
    let_num = dict(map(lambda i, j: i+j, 'ABCDEFG', '0123456'))
    # print(let_num)
    for column, color in moves:
        grid[int(let_num[column])] += color
    # print(grid)
    print(v_check(grid))
    v = v_check(grid)
    print(h_check(grid))
    h = h_check(grid)
    # print('first grid', grid)
    print('d1 =', d1_check(grid))
    d1 = d1_check(grid)
    # print('second grid', grid)
    print(d2_check(grid))
    d2 = d2_check(grid)

    if v == 'y' or h == 'y' or d1 == 'y' or d2 == 'y':
        print('Yellow')
        return 'Yellow'
    elif v == 'r' or h == 'r' or d1 == 'r' or d2 == 'r':
        print('Red')
        return 'Red'
    else:
        print('Draw')
        return 'Draw'


moves = [
    "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow",
    "G_Red", "C_Yellow", "C_Red", "D_Yellow", "F_Red", "E_Yellow", "A_Red",
    "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", "B_Yellow",
    "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]
winner = "Yellow"
who_is_winner(moves)
