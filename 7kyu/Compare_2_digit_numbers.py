from timeit import default_timer as timer
import re

start = timer()
qq = print


# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.
# Example:
# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.


def compare(a, b):
    """ returns % of matching """

    a, b = set(str(a)), set(str(b))
    if a == b:
        return '100%'
    if a.isdisjoint(b):
        return '0%'
    else:
        return '50%'


def tests():
    assert compare(10, 11) == "50%"
    assert compare(33, 33) == "100%"
    assert compare(45, 45) == "100%"
    assert compare(14, 24) == "50%"
    assert compare(56, 57) == "50%"
    assert compare(38, 84) == "50%"
    assert compare(10, 22) == "0%"
    assert compare(11, 44) == "0%"
    assert compare(98, 70) == "0%"
    assert compare(66, 16) == "50%"
    assert compare(98, 88) == "50%"
    assert compare(78, 58) == "50%"
    assert compare(47, 56) == "0%"


a, b = 33, 33
qq(compare(a, b))
tests()



end = timer()
print(end - start)
