from timeit import default_timer as timer
import itertools as it

start = timer()
qq = print


# https://www.codewars.com/kata/5cc2cd9628b4200020880248


def reduce_pyramid(base):
    """ returns the pyramid's top """

    # 1) special case of one input element handler

    # 2) building a list of a row coefficients, e.g. [1, 4, 6, 4, 1] for [n1, n2, n3, n4, n5, n6]
    #    according to Pascal's triangle

    # 3) building summation pairs, e.g. [(1, 2), (2, 3), (3, 4)] for base = [1, 2, 3, 4]

    # 4) put coef and pairs lists together

    # 5) calculating and returning the final sum (pyramid's top)

    if len(base) == 1:
        return base[0]

    coef = [1]
    for i in range(1, len(base) - 1):
        coef.append(int(coef[i - 1] * ((len(base) - 2) + 1 - i) // i))

    x = list(it.pairwise(base))

    y = list(zip(coef, x))

    return sum([i[0] * sum(i[1]) for i in y])


# first solution (similar to the second, but recursive)
# failed because of 999 python recursion limit
#
# second solution
# failed because of slow performance
# Execution Timed Out (12000 ms)
#
# def reduce_pyramid(base):
#     if len(base) == 1:
#         return base[0]
#     x = [sum(i) for i in list(it.pairwise(base))]
#     for i in range(len(base) - 2):
#         x = [sum(i) for i in list(it.pairwise(x))]
#     return x[0]


base = [1, 2, 3, 4]
qq(reduce_pyramid(base))

end = timer()
print(end - start)
