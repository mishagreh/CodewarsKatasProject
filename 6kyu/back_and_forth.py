from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/63624a696137b6000ed726a6

def minimum_amount(lst: list) -> tuple:
    """ returns minimal initial number of boxes for first and second side """

    if not lst:
        lst = [0, 0]
    if len(lst)%2 == 1:
        lst = lst + [0]

    balance1 = lst[0]
    balance2 = 0
    moves1 = [lst[i] for i, j in enumerate(lst) if not i%2]
    moves2 = [lst[i] for i, j in enumerate(lst) if i%2]
    delta1 = []
    delta2 = []

    for i in range(len(moves1)):
        balance1 = balance1 - moves1[i]
        balance2 = balance2 + moves1[i]
        delta1.append(balance1)
        balance1 = balance1 + moves2[i]
        balance2 = balance2 - moves2[i]
        delta2.append(balance2)

    if min(delta1) < 0:
        balance1_init = abs(min(delta1)) + lst[0]
    else:
        balance1_init = lst[0]
    if min(delta2) < 0:
        balance2_init = abs(min(delta2))
    else:
        balance2_init = 0

    return balance1_init, balance2_init


lst = [53, 88, 40, 154, 149, 121, 53, 188, 194]
# lst = [4, 3, 2, 1]
# lst = [1, 2, 3, 4]
print(minimum_amount(lst))

end = timer()
print(end - start)
