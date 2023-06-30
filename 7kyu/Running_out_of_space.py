from timeit import default_timer as timer
# import math

start = timer()
qq = print

# Kevin is noticing his space run out! Write a function that removes the spaces from the values and
# returns an array showing the space decreasing.
# For example, running this function on the array ['i', 'have','no','space'] would
# produce ['i','ihave','ihaveno','ihavenospace']


def spacey(array):
    """ returns the list where each next iterable is equal to the concatenation of all previous iterables """

    res = [array[0]]
    for i in range(1, len(array)):
        res.append(res[i-1] + array[i])
    return res

# best practices
# from itertools import accumulate
# def spacey(a):
#     return list(accumulate(a))
#
# def spacey(array):
#     return [''.join(array[:i+1]) for i in range(len(array))]

def fixed_tests():
    assert spacey(['kevin', 'has', 'no', 'space']) == ['kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace']
    assert spacey(['this', 'cheese', 'has', 'no', 'holes']) == \
           ['this', 'thischeese', 'thischeesehas', 'thischeesehasno', 'thischeesehasnoholes']


array = ['i', 'have','no','space']
qq(spacey(array))
fixed_tests()

end = timer()
print(end - start)
