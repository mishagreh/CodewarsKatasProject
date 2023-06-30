from timeit import default_timer as timer

start = timer()
qq = print

# https://www.codewars.com/kata/559e10e2e162b69f750000b4
# A zero-indexed array arr consisting of n integers is given.
# The dominator of array arr is the value that occurs in more than half of the elements of arr.
# For example, consider array arr such that arr = [3,4,3,2,3,1,3,3]
# The dominator of arr is 3 because it occurs in 5 out of 8 elements of arr and 5 is more than a half of 8.
# Write a function dominator(arr) that, given a zero-indexed array arr consisting of n integers,
# returns the dominator of arr. The function should return −1 if array does not have a dominator.
# All values in arr will be >=0.


def dominator(arr):
    """
    Returns the dominator of arr.
    """

    if arr:
        res = [(arr.count(x), x) for x in set(arr)]
        if max(res)[0] > len(arr) / 2:
            return max(res)[1]
    return -1


def fixed_tests():
    assert dominator([3, 4, 3, 2, 3, 1, 3, 3]) == 3
    assert dominator([1, 2, 3, 4, 5]) == -1
    assert dominator([1, 1, 1, 2, 2, 2]) == -1
    assert dominator([1, 1, 1, 2, 2, 2, 2]) == 2
    assert dominator([]) == -1


# arr = []
arr = [3, 4, 3, 2, 3, 1, 3, 3]
qq(dominator(arr))
fixed_tests()

end = timer()
print(end - start)
