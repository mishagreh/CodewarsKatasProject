from timeit import default_timer as timer
import itertools as it

start = timer()
qq = print


# https://www.codewars.com/kata/64d482b76fad180017ecef0a


# have no my own fast solution
# but this one is the most understandable for me and the closest to my recursive solution in divide_and_conquer.py
#
# a29813287
# from collections import Counter
#
# def consecutive_nums(lst, group_len):
#     lst = Counter(lst)
#     while lst:
#         x = min(lst)
#         for i in range(group_len):
#             if x + i not in lst:
#                 return False
#             lst[x + i] -= 1
#             if lst[x + i] == 0:
#                 lst.pop(x + i)
#     return True


# lst, group_len = [1, 2, 3, 4, 1, 2, 3, 4, 6, 7, 8, 9], 4
# lst, group_len = [1, 2, 3, 6, 2, 3, 4, 7, 8], 3
lst, group_len = [4, 3, 2, 1], 2
# lst, group_len = [2, 3, 4, 5, 3, 6, 7, 4, 5], 3
print(consecutive_nums(lst, group_len))


end = timer()
print(end - start)
