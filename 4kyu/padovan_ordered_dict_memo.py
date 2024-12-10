# https://www.codewars.com/kata/5819f1c3c6ab1b2b28000624
#
# Description:
# The Padovan sequence is the sequence of integers P(n) defined by the initial
# values
# P(0)=P(1)=P(2)=1
# and the recurrence relation
# P(n)=P(n-2)+P(n-3)
# The first few values of P(n) are
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200,
# 265, ...
# Task
# The task is to write a method that returns i-th Padovan number for i around
# 1,000,000
# Hint: use matrices

from collections import OrderedDict


n = 1000


def padovan_util(n, memo):
    try:
        if memo[str(n)]:
            return memo[str(n)]
    except KeyError:
        # print('failed attempt, there is no', n)
        # print(memo)
        memo[str(n)] = padovan_util(n-2, memo) + padovan_util(n-3, memo)
        memo.popitem(last=False)
        return memo[str(n)]


def padovan(n):
    memo = OrderedDict.fromkeys('01234')
    for i, j in enumerate('11122'):
        memo[str(i)] = int(j)
    # print(memo)
    return padovan_util(n, memo)


print(padovan(n))
