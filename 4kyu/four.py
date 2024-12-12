# https://www.codewars.com/kata/56882731514ec3ec3d000009
import pdb


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
    print(grid_h)
    for i, column in enumerate(grid):
        for j, row in enumerate(column):
            grid_h[j] += row

    print(grid_h)
    for column in grid_h:
        for color in ('r', 'y'):
            if column.find(3*color) != -1:
                return color
    return


def who_is_winner(moves):
    grid = ['' for i in range(7)]
    moves = list(map(lambda i: (i[0], 'y' if i[2] == 'Y' else 'r'), moves))
    print(moves)
    let_num = dict(map(lambda i, j: i+j, 'ABCDEFG', '0123456'))
    print(let_num)
    for column, color in moves:
        grid[int(let_num[column])] += color
    print(grid)
    print(v_check(grid))
    print(h_check(grid))


moves = [
    "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow",
    "G_Red", "C_Yellow", "C_Red", "D_Yellow", "F_Red", "E_Yellow", "A_Red",
    "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", "B_Yellow",
    "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]
winner = "Yellow"
who_is_winner(moves)
