from timeit import default_timer as timer
# import math

start = timer()
qq = print

# Rick wants a faster way to get the product of the largest pair in an array.
# Your task is to create a performant solution to find the product of the largest two integers
# in a unique array of positive numbers.
# All inputs will be valid.
# Passing [2, 6, 3] should return 18, the product of [6, 3].
#
# Disclaimer: only accepts solutions that are faster than his, which has a running time O(nlogn).
#
# max_product([2, 1, 5, 0, 4, 3])              # => 20
# max_product([7, 8, 9])                       # => 72
# max_product([33, 231, 454, 11, 9, 99, 57])   # => 104874

def max_product(a):
    """
    Returns the product of the largest two integers
    """

    # my fastest algorithm
    res = []
    for i in range(2):
        res.append(max(a))
        a.remove(max(a))
    return res[0]*res[1]

    # my second fastest algorithm
    # res = []
    # for i in range(2):
    #     res.append(max(a))
    #     a.remove(max(a))
    # return math.prod(res)

    # Performance test: should not be too slow
    # Too slow! Speed: 0.56712s
    # Limit: 0.23300s. Maybe try a different approach?
    # return sorted(a)[-2]*sorted(a)[-1]

    # Performance test: should not be too slow
    # Too slow! Speed: 0.28182s
    # Limit: 0.22822s. Maybe try a different approach?
    # return math.prod(sorted(a)[-2:])


def fixed_tests():
    assert max_product([56, 335, 195, 443, 6, 494, 252]) == 218842
    assert max_product([154, 428, 455, 346]) == 194740
    assert max_product([39, 135, 47, 275, 37, 108, 265, 457, 2, 133, 316, 330, 153, 253, 321, 411]) == 187827
    assert max_product([136, 376, 10, 146, 105, 63, 234]) == 87984
    assert max_product([354, 463, 165, 62, 472, 53, 347, 293, 252, 378, 420, 398, 255, 89]) == 218536
    assert max_product([346, 446, 26, 425, 432, 349, 123, 269, 285, 93, 75, 14]) == 192672
    assert max_product([134, 320, 266, 299]) == 95680
    assert max_product([114, 424, 53, 272, 128, 215, 25, 329, 272, 313, 100, 24, 252]) == 139496
    assert max_product([375, 56, 337, 466, 203]) == 174750


a = [39, 135, 47, 275, 37, 108, 265, 457, 2, 133, 316, 330, 153, 253, 321, 411]
qq(max_product(a))
fixed_tests()

end = timer()
print(end - start)
