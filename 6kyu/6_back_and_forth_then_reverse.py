from timeit import default_timer as timer
import math

start = timer()
qq = print


# https://www.codewars.com/kata/60cc93db4ab0ae0026761232

def arrange(s: str) -> list:
    """returns a list, generated according to the given rules"""

    iter_num = math.ceil(len(s) / 2)
    even_element = 0
    odd_element = -1
    d = []

    for i in range(iter_num):
        if i % 2 == 0:
            d.extend([s[even_element], s[odd_element]])
        else:
            d.extend([s[odd_element], s[even_element]])
        even_element += 1
        odd_element -= 1

    return d if len(s) % 2 == 0 else d[:-1]


s = [1, 2, 3, 4, 5]
print(arrange(s))

end = timer()
print(end - start)
