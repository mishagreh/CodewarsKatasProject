from timeit import default_timer as timer
from string import ascii_lowercase as alc
from itertools import pairwise as pw

start = timer()
qq = print


# https://www.codewars.com/kata/64c45287edf1bc69fa8286a3

def solution(s):
    ind = []
    for i in s:
        if i in alc:
            ind.append(alc.index(i))
    z = tuple(pw(ind))
    y = []
    for i in z:
        y.append(i[1] - i[0])
    return ind, z, y


s = 'abcxdef'
print(solution(s))

end = timer()
print(end - start)
