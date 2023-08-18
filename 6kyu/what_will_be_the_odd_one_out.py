from timeit import default_timer as timer
from collections import Counter

start = timer()
qq = print


# https://www.codewars.com/kata/55b080eabb080cd6f8000035

def odd_one_out(s):

    x = Counter(s)

    y = []
    for i in s[::-1]:
        if x[i] % 2:
            y.append(i)
            x[i] = 2

    return y[::-1]

# best solution
# def odd_one_out(s):
#     d = Counter(reversed(s))
#     return [x for x in d if d[x] % 2][::-1]


s = 'Hello World'
print(odd_one_out(s))

end = timer()
print(end - start)
