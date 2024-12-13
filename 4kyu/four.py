# https://www.codewars.com/kata/56882731514ec3ec3d000009
import pdb
import numpy as np


def check_columns_rows(grid, direction):

    if direction == 'columns':
        gr = grid.copy()
    elif direction == 'rows':
        # transpose grid horizontally
        gr = ['' for i in range(7)]
        for i, column in enumerate(grid):
            for j, row in enumerate(column):
                gr[j] += row

    # look for 4-sequence in rows/columns
    for column in gr:
        for color in ('r', 'y'):
            if column.find(4*color) != -1:
                return color
    return


def check_diagonals(grid, diagonal):
    gr = grid.copy()
    for i, column in enumerate(gr):
        c = column[::-1].zfill(6)
        gr[i] = list(c[::-1])
    gr_np = np.array(gr)
    diags = []
    for i in range(-6, 6):
        if diagonal == 'main':
            diags.append(''.join(gr_np.diagonal(i)))
        elif diagonal == 'anti':
            diags.append(''.join(np.flipud(gr_np).diagonal(i)))
    # shortest diags removed (3 leftmost and 3 rightmost)
    for column in diags[3:9]:
        for color in ('r', 'y'):
            if column.find(4*color) != -1:
                return color
    return


def who_is_winner(moves):
    # create empty grid
    grid = ['' for i in range(7)]
    # reshape moves
    moves = list(map(lambda i: (i[0], 'y' if i[2] == 'Y' else 'r'), moves))
    letter_number_converter = dict(map(lambda i, j: i+j, 'ABCDEFG', '0123456'))
    # go and analyze move by move
    steps = []
    for move in moves:

        steps.append(move)
        gr = grid.copy()
        for column, color in steps:
            gr[int(letter_number_converter[column])] += color
        for i, column in enumerate(gr):
            c = column[::-1].zfill(6)
            gr[i] = c[::-1]

        v = check_columns_rows(gr, direction='columns')
        h = check_columns_rows(gr, direction='rows')
        d1 = check_diagonals(gr, diagonal='main')
        d2 = check_diagonals(gr, diagonal='anti')

        match (v or h or d1 or d2):
            case 'y': return 'Yellow'
            case 'r': return 'Red'
            case _: continue

    return 'Draw'


moves = [
    "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow",
    "G_Red", "C_Yellow", "C_Red", "D_Yellow", "F_Red", "E_Yellow", "A_Red",
    "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", "B_Yellow",
    "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]
winner = "Yellow"
who_is_winner(moves)
