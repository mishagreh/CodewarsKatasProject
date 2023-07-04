from timeit import default_timer as timer

start = timer()
qq = print

#  https://www.codewars.com/kata/5821cd4770ca285b1f0001d5


def snakes_and_ladders(board, dice):
    """ returns the latest board position number """

    bp = 0  # = board position
    mn = 0  # = move_number

    while mn < len(dice):
        if (bp + dice[mn]) < len(board):
            bp += dice[mn]
            if board[bp] != 0:
                bp += board[bp]
        mn += 1
    return bp

# def tests():


board, dice = [0, 0, 0, 0, 0], [1, 1, 1]
qq(snakes_and_ladders(board, dice))
# tests()

end = timer()
print(end - start)
