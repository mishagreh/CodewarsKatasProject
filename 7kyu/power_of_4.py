from timeit import default_timer as timer
import math

start = timer()
qq = print


# https://www.codewars.com/kata/544d114f84e41094a9000439


def powerof4(n):
    """ returns true if a given parameter is a power of 4, and false if it's not """

    return False if type(n) != int or n < 0 else (math.log(n, 4)).is_integer()


n = 16
qq(powerof4(n))
# tests()


end = timer()
print(end - start)
