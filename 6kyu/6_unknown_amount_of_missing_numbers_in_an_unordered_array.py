from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/5b559899f7e38620ef000803

def miss_nums_finder(arr):
    """ returns the missing numbers sorted by value """

    x = set(arr)
    y = set(range(1, max(arr)+1))
    return sorted(list(y-x))


arr = [7, 1, 12, 9, 11, 14, 13, 6, 10, 5]
print(miss_nums_finder(arr))

end = timer()
print(end - start)
