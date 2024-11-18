# https://www.codewars.com/kata/59031db02b0070a923000110

n = 3
s = [[1, 1, 0], [1, 0, 0], [0, 1, 1]]

# [1,1,0]
# n = 1
# s = [[1, 1, 0, 1]]


def _(n, s):
    a = list(map(lambda x: int(sum(x) > n/2), list(zip(*s))))
    print(a)

# proper solution, passed all the tests (whitespaces don't matter)
# 'zero_or_one' instead of 'b'
b = lambda n,s:[int(sum(i)>n/2) for i in zip(*s)]

_(n, s)
print(b(n, s))
