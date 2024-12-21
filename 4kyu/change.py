# https://www.codewars.com/kata/541af676b589989aed0009e7
#
#
from itertools import product, combinations, permutations


def count_change(money, coins, n=0, res=0, res2=[]):
    # your implementation here
    n = len(coins)
    coins = sorted(coins)[::-1]
    print('coins:', coins)
    # x(money) = n(n) + (n-1)n + (n-2)n
    # res = 0
    print('div:', money % sum(coins))
    if money % sum(coins) == 0:
        res += 1
        res2.append(coins)
    print('res:', res)

    for i in coins:
        if money % i == 0:
            print('yes')
            res += 1
            if i not in res2:
                res2.append(i)
    print(res)
    print(res2)

    n -= 1
    if n >= 2:
        z = list(combinations(coins, n))
        print('z:', z)
        # if n >= 1:
        for i in z:
            print('recur')
            print(count_change(money, i, n, res, res2))
    # else:
            # return 'second end', res
    else:
        print('n = 2')
        return 'first end', res, res2, len(res2)
    print('n:', n)


print(count_change(6, [1, 2]))
# 4
# print(count_change(4, [1, 2]))
# 1+1+1+1, 1+1+2, 2+2
# print(count_change(10, [5, 2, 3]))
# 4
# print(count_change(11, [5, 7]))
# 0
# print(count_change(0, [1, 2]))
# 1
# print(event) or something_else(and):
