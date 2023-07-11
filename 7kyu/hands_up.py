from timeit import default_timer as timer
import math

start = timer()
qq = print


# https://www.codewars.com/kata/56d8f14cba01a83cdb0002a2


def get_positions(n):
    """
        returns an array representing the number
        of hands raised by each person at that step
    """

    return n % 3, int((n % 9) / 3), int((n % 27) / 9)


n = 9
qq(get_positions(n))
# tests()


end = timer()
print(end - start)
