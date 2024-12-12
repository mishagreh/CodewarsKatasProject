# https://www.codewars.com/kata/599385ae6ca73b71b8000038
from collections import deque


def ant_bridge(ants, terrain):
    a = deque(ants)
    # move = lambda: a.appendleft(a.pop())
    def move(): a.appendleft(a.pop())
    pp = p = ''  # pre-previous, previous, current iterable
    for i in terrain:
        if (i == '.' and p == '-'):
            if pp == '.':
                move()
            else:
                move()
                move()
        elif (i == '.' and p == '.') or (i == '-' and p == '.'):
            move()
        pp, p = p, i

    return ''.join(a)


ants = "GFEDCBA"
terrain = "------....-.---"
# 'GFEDCBA' should equal 'AGFEDCB'
# print(ant_bridge(ants, terrain))
print(ant_bridge(ants, terrain))
