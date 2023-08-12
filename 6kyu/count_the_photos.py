from timeit import default_timer as timer
import itertools as it

start = timer()
qq = print


# https://www.codewars.com/kata/6319dba6d6e2160015a842ed

def count_photos(road):
    """
        returns the total number of photos that were taken by the cameras.
        The complexity should be strictly O(N) in order to pass all the tests.
    """

    count_r, count_l, cross_r, cross_l = 0, 0, 0, 0

    for j in road:
        if j == '>':
            count_r += 1
        elif j == '.':
            cross_r += count_r

    for j in road[::-1]:
        if j == '<':
            count_l += 1
        elif j == '.':
            cross_l += count_l

    return cross_r + cross_l


road = ">.>..<"
print(count_photos(road))

end = timer()
print(end - start)
