from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/60e4dfc1dc28e70049e2cb9d


def strings_in_max_depth(s):

    """ returns the max depth strings """

    parsed, open_count = [], 0
    open_count_ls = []

    for j, i in enumerate(s):
        if i == '(':
            open_count += 1
            open_count_ls.append(open_count)
            parsed.append(((open_count, 'open'), j))
        elif i == ')':
            parsed.append(((open_count, 'close'), j))
            open_count -= 1

    if not parsed:
        return [s]

    max_depth = max(open_count_ls)
    res_indexes = [i[1] for i in parsed if i[0] == (max_depth, 'open') or i[0] == (max_depth, 'close')]

    return [s[res_indexes[i] + 1:res_indexes[i + 1]] for i in range(0, len(res_indexes), 2)]


# s = "AA(XX)(YY)(U)"
# s = "(A(B))"
# s = "((A)B)"
s = "AA(XX((YY))(U))"
# s = "AA((XX))(YY)(U)"
# s = "AA((XX)(YY))(U)"
print(strings_in_max_depth(s))

end = timer()
print(end - start)
