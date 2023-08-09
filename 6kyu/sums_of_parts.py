from timeit import default_timer as timer
import itertools as it

start = timer()
qq = print


# https://www.codewars.com/kata/5ce399e0047a45001c853c2b


# solution 1
# Execution Timed Out (12000 ms)
#
# def parts_sums(ls):
#     return [sum(ls[i:]) for i in range(len(ls)+1)]


# solution 2
# works good
# def parts_sums(ls):
#     res = [0]
#     for i in range(len(ls)):
#         res.append(res[-1] + ls[~i])
#     return list(reversed(res))

# solution 3
# simplified 2

def parts_sums(ls):
    res = [0]
    for i in reversed(ls):
        res.append(res[-1] + i)
    return res[::-1]


ls = [1, 2, 3, 4, 5, 6]
print(parts_sums(ls))

end = timer()
print(end - start)
