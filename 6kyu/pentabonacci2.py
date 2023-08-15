from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/55c9172ee4bb15af9000005d

def pentaFib(n, memo):
    """ returns the last number + all numbers dictionary """

    f = pentaFib

    if n in memo:
        return memo[n], memo

    memo[n] = f(n - 1, memo)[0] + f(n - 2, memo)[0] + f(n - 3, memo)[0] + f(n - 4, memo)[0] + f(n - 5, memo)[0]

    return memo[n], memo


def count_odd_pentaFib(n):
    """ counts the odd numbers in the all numbers dictionary """

    if not n:
        return 0

    memo = {0: 0, 1: 1, 2: 1, 3: 2, 4: 4}
    memo = pentaFib(n, memo)[1]

    return len([memo[i] for i in memo if memo[i] % 2]) - 1


n = 2
print(count_odd_pentaFib(n))

# the shortest solution
#
# def count_odd_pentaFib(n):
#     return 2 * (n // 6) + [0, 1, 2, 2, 2, 2][n % 6] - (n >= 2)


# the solution i liked the most and understood
#
# saudiGuy
# def count_odd_pentaFib(n):
#     x = [0, 1, 1, 2, 4]
#     while len(x)<=n:
#         x += [sum(x[-5:])]
#     return 0 if n==0 else sum(1 for i in set(x) if i%2)

end = timer()
print(end - start)
