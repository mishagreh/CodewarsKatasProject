# https://www.codewars.com/kata/59547688d8e005759e000092


def distribution_of(golds):
    left, right, res = 0, -1, [0, 0]
    for move in range(len(golds)):
        if golds[left] < golds[right]:
            pile = golds[right]
            right -= 1
        else:
            pile = golds[left]
            left += 1
        res[move % 2] += pile
    print(res)
    return res


distribution_of([4, 7, 2, 9, 5, 2])
# [11, 18]
distribution_of([10, 1000, 2, 1])
# [12, 1001]
