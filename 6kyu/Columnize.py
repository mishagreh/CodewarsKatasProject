from timeit import default_timer as timer
import itertools

start = timer()
qq = print

#  https://www.codewars.com/kata/6087bb6050a6230049a068f1


def columnize(items, columns_count):

    #  to handle a case  if the number of items is less than a number of columns_count var
    proper_range = range(min(columns_count, len(items)))

    #  number of columns list, e.g. [0, 1, 2] for 3 columns
    columns_count_list = [i for i in proper_range]

    #  each item is specified with a column number within the nested list,
    #  e.g. [[0, '1'], [1, '12'], [2, '123'], [0, '1234'], [1, '12345'], [2, '123456']]
    column_item_list = [[b, a] for a, b in zip(items, itertools.cycle(columns_count_list))]

    #  returning a list of the longest strings in each column, e.g. [10, 5, 6] for 3 columns
    longest = [len(max([z[1] for z in column_item_list if z[0] == n], key=len)) for n in proper_range]

    #  adding whitespaces and separators ('|') to each string
    #  the rightmost column has no right separator
    #  the rightmost string in the lowest row has no right separator as well
    for n in proper_range:
        for k in column_item_list:
            if k[0] == n - 1 and column_item_list.index(k) != (len(column_item_list) - 1):
                k[1] = k[1] + (longest[n - 1] - len(k[1])) * ' ' + ' | '
            if k[0] == n:
                k[1] = k[1] + (longest[n] - len(k[1])) * ' '

    #  adding '\n' character to each first string in a row except the very first row
    for i in range(len(items)):
        if i % columns_count == 0 and i != 0:
            column_item_list[i][1] = '\n' + column_item_list[i][1]

    #  each string of the list is modified and which can be transformed into a result string now

    return ''.join([y[1] for y in column_item_list])


# the shortest solution (not mine, of course) to analyze
#
# from itertools import zip_longest
#
# def columnize(a, n):
#     a = [a[i:i+n] for i in range(0, len(a), n)]
#     b = [max(map(len, x)) for x in zip_longest(*a, fillvalue="")]
#     return "\n".join(" | ".join(y.ljust(z) for y, z in zip(x, b)) for x in a)

# def tests():


items, columns_count = ["1", "12", "123", "1234", "12345", "123456"], 3
qq(columnize(items, columns_count))
# tests()

end = timer()
print(end - start)