from timeit import default_timer as timer
import itertools as it

start = timer()
qq = print


# https://www.codewars.com/kata/5a5cdb07fd56cbdd3c00005b


def find_dups_miss(arr):

    """ returns a missing number and duplicates array. Long input arrays compatible """

    x = list(it.pairwise(sorted(arr)))
    for i in x:
        if i[1] - i[0] == 2:
            y = i[0] + 1
    z = [i[0] for i in x if i[0] == i[1]]

    return [y, z]


arr = [20, 19, 6, 9, 7, 17, 16, 17, 12, 5, 6, 8, 9, 10, 14, 13, 11, 14, 15, 19]
qq(find_dups_miss(arr))
end = timer()
print(end - start)
