# https://www.codewars.com/kata/5263c6999e0f40dee200059d
#
# '8', ['5','7','8','9','0']
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
import math


numbers = '111'


def combine(alts):
    for num in range(len(alts)-1):
        combined = []
        for sub in alts[-2]:
            for k in alts[-1]:
                combined.append(sub+k)
        alts = alts[:-2] + [combined.copy()]
    return alts[0]


def get_pins(numbers):
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['l', '0', 'r']
    ]
    nexts = {}
    for row in keypad:
        for digit in row:
            nexts.setdefault(digit, (row.index(digit), keypad.index(row)))
    alts = []
    for num in numbers:
        alts.append(list(filter(
            lambda x:
                math.dist(nexts[num], nexts[x]) <= 1 and x not in ('l', 'r'),
            nexts
        )))
    return combine(alts)


print(get_pins(numbers))

li = [['1', '2', '4'], ['1', '2', '4'], ['1', '2', '4']]
# print(recur(li))
