from timeit import default_timer as timer
import itertools as it

start = timer()
qq = print


# https://www.codewars.com/kata/5b4dee5d05f04bba43000138

def f(n):
    """ returns f(n) value """

    dr = sum(int(i) for i in str(n))
    dsddr = sum(int(i) ** 2 for i in str(dr))
    return dr + dsddr


def key_func(x):
    """ provides key func for itertools.groupby """

    return x[0]


def sorted_comm_by_digs(arr1, arr2):
    """
        returns an array with the common elements occurring once an d sorted
        by their corresponding value of f in descending order
    """

    z = set(arr1).intersection(set(arr2))
    x = sorted(((f(n), n) for n in z))
    groups = [list(group) for key, group in it.groupby(x, key_func)][::-1]
    res = []
    for i in groups:
        if len(i) == 1:
            res.append(i[0][1])
        else:
            for j in i:
                res.append(j[1])
    return res


# best solution

# def f(n):
#     dr = sum(map(int, str(n)))
#     deep = sum(d * d for d in map(int, str(dr)))
#     return (-dr - deep, n)
#
#
# def sorted_comm_by_digs(arr1, arr2):
#     return sorted(set(arr1) & set(arr2), key=f)


arr1, arr2 = [5, 56, 28, 35, 12, 27, 64, 99, 18, 31, 14, 6], [28, 17, 31, 63, 64, 5, 18, 17, 95, 56, 37, 5, 28, 16]
qq(sorted_comm_by_digs(arr1, arr2))

end = timer()
print(end - start)
