from timeit import default_timer as timer
import re

start = timer()
qq = print


def binary_pyramid(m, n):
    return bin(sum([int(bin(i)[2:]) for i in range(m, n + 1, 1)]))[2:]

    # while and more readable solution
    #
    # i = m
    # med = []
    # while i <= n:
    #     med.append(int(bin(i)[2:]))
    #     i += 1
    # qq(med)
    # return bin(sum(med))[2:]



def tests():
    assert binary_pyramid(1, 4) == "1111010"
    assert binary_pyramid(1, 6) == "101001101"
    assert binary_pyramid(6, 20) == "1110010110100011"
    assert binary_pyramid(21, 60) == "1100000100010001010100"


m,n = 1, 4
qq(binary_pyramid(m,n))
tests()





end = timer()
print(end - start)
