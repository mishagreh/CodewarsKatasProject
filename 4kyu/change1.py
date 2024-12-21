# https://www.codewars.com/kata/541af676b589989aed0009e7
#
#
from itertools import product, combinations, permutations


def count_change(money, coins, n=0, res=0, res2=[]):
    m = [money // i for i in coins]
    # print('m:', m)
    mu = [list(range(i+1)) for i in m]
    # print('mu', mu)
    for num, item in enumerate(coins):
        for number, it in enumerate(mu[num]):
            mu[num][number] = it*item
    # print(mu)
    z = list(product(*mu))
    # print(z)
    res = 0
    for item in z:
        # print(item)
        if sum(item) == money:
            res += 1
    print(res)



# print(count_change(6, [1, 2]))
# 4
# print(count_change(4, [1, 2]))
# count_change(4, [1, 2])
# 1+1+1+1, 1+1+2, 2+2
# print(count_change(10, [5, 2, 3]))
# 4
# print(count_change(11, [5, 7]))
# 0
print(count_change(0, [1, 2]))
# 1
# print(event) or something_else(and):
