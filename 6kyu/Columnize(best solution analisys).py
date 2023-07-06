from timeit import default_timer as timer
from itertools import zip_longest

start = timer()
qq = print

#  https://www.codewars.com/kata/6087bb6050a6230049a068f1


def columnize(a, n):
    a = [a[i:i+n] for i in range(0, len(a), n)]
    b = [max(map(len, x)) for x in zip_longest(*a, fillvalue="")]
    return "\n".join(" | ".join(y.ljust(z) for y, z in zip(x, b)) for x in a)

# def tests():


a, n = ["1", "12", "123", "1234", "12345", "123456"], 3
qq(columnize(a, n))
# tests()

end = timer()
print(end - start)