from timeit import default_timer as timer

start = timer()
qq = print


def find_even_index(arr):
    """
    returns index where the sum of the integers to the left of it is equal to the sum of the integers to the
    right of i. If there is no index that would make this happen, return -1
    """

    for i, j in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1



def tests():
    assert find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3
    assert find_even_index([1, 100, 50, -51, 1, 1]) == 1
    assert find_even_index([1, 2, 3, 4, 5, 6]) == -1
    assert find_even_index([20, 10, 30, 10, 10, 15, 35]) == 3
    assert find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0
    assert find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6
    assert find_even_index(list(range(1, 100))) == -1
    assert find_even_index([0, 0, 0, 0, 0]) == 0
    assert find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3
    assert find_even_index(list(range(-100, -1))) == -1


arr = [1, 2, 3, 4, 3, 2, 1]
qq(find_even_index(arr))
tests()

end = timer()
print(end - start)
