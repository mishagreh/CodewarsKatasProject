from timeit import default_timer as timer
import itertools as it

start = timer()
qq = print


# https://www.codewars.com/kata/64d482b76fad180017ecef0a

# def consecutive_nums(lst, group_len):
#     res = [(i[1] - i[0]) for i in it.pairwise(lst)]
#     return res.count(1) >= group_len

def consecutive_nums(lst, group_len):

    if not lst or len(lst) < group_len:
        return False

    x = min(lst)
    lst.remove(x)
    for i in range(group_len - 1):
        if (x + 1) in lst:
            lst.remove(x + 1)
            x = x + 1
        else:
            return False

    consecutive_nums(lst, group_len)

    return not lst


lst, group_len = [6, 6, 6, 9, 7, 8, 7, 5, 8, 5, 7, 8], 4
# lst, group_len = [2, 3, 4, 5], 2
# lst, group_len = [2, 3, 4, 5, 3, 6, 7, 4, 5], 3
print(consecutive_nums(lst, group_len))


end = timer()
print(end - start)
