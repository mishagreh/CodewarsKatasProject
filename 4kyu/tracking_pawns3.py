from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/56b012bbee8829c4ea00002c

def pawn_move_tracker(moves: list) -> list:
    """ returns the board state after all the moves """

    board = [
                [".", ".", ".", ".", ".", ".", ".", "."],
                ["p", "p", "p", "p", "p", "p", "p", "p"],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                [".", ".", ".", ".", ".", ".", ".", "."]
            ][::-1]

    # no moves edge case verification
    if not moves:
        return board[::-1]

    # verifying if the first 2 moves (1 white and 1 black) are valid
    if len(moves):
        if moves[0][-1] not in ('3', '4'):
            return f'{moves[0]} is invalid'
    else:
        if moves[0][-1] not in ('3', '4'):
            return f'{moves[0]} is invalid'
        if moves[1][-1] not in ('5', '6'):
            return f'{moves[1]} is invalid'

    # converting the move letters into numbers, to use as list/str indexes
    vert = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    moves_num = [['', int(i[-1]) - 1, vert[i[0]]] if len(i) == 2
                 else [vert[i[0]], int(i[-1]) - 1, vert[i[-2]]] for i in moves]

    # capture moves verification (both letters and digits)
    for i, j in enumerate(moves_num):
        if moves_num[i][0] != '':
            if abs(moves_num[i][2] - moves_num[i][0]) != 1 or moves_num[i][1] - moves_num[i - 2][1] > 1:
                return f'{moves[i]} is invalid'

    # board state changes, move by move, for b/w and move/capture
    w = []  # white move letters tracking to monitor the first double space move for each letter
    b = []  # black move letters tracking to monitor the first double space move for each letter
    i = 0
    while i <= len(moves) - 1:
        if i % 2:  # choose b/w
            if moves_num[i][0] == '':  # choosing move/capture
                if board[moves_num[i][1]][moves_num[i][2]] == '.':
                    board[moves_num[i][1]][moves_num[i][2]] = 'p'
                    board[moves_num[i][1] + (2 if moves_num[i][2] not in b and moves_num[i][1] == 4 else 1)] \
                        [moves_num[i][2]] = '.'
                    b.append(moves_num[i][2])
                    i += 1
                else:
                    return f'{moves[i]} is invalid'
            else:
                if board[moves_num[i][1]][moves_num[i][2]] == 'P':
                    board[moves_num[i][1]][moves_num[i][2]] = 'p'
                    board[moves_num[i - 2][1]][moves_num[i - 2][2]] = '.'
                    i += 1
                else:
                    return f'{moves[i]} is invalid'
        else:
            if moves_num[i][0] == '':  # choosing move/capture
                if board[moves_num[i][1]][moves_num[i][2]] == '.':
                    board[moves_num[i][1]][moves_num[i][2]] = 'P'
                    board[moves_num[i][1] - (2 if moves_num[i][2] not in w and moves_num[i][1] == 3 else 1)] \
                        [moves_num[i][2]] = '.'
                    w.append(moves_num[i][2])
                    i += 1
                else:
                    return f'{moves[i]} is invalid'
            else:
                if board[moves_num[i][1]][moves_num[i][2]] == 'p':
                    board[moves_num[i][1]][moves_num[i][2]] = 'P'
                    board[moves_num[i - 2][1]][moves_num[i - 2][2]] = '.'
                    i += 1
                else:
                    return f'{moves[i]} is invalid'

    return board[::-1]


moves = ['a3', 'h6', 'a4', 'h5', 'a5', 'h4', 'a6', 'h3', 'axb7', 'hxg2']
print(pawn_move_tracker(moves))

end = timer()
print(end - start)
