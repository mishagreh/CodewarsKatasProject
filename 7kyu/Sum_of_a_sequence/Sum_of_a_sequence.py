from timeit import default_timer as timer
# import math

start = timer()
qq = print


def sequence_sum(begin_number, end_number, step):
    """ returns the sum of a sequence of integers """

    nums = []
    i = begin_number
    while i <= end_number:
        nums.append(i)
        i += step
    return sum(nums)


# the shortest solution with the highest best practice rate
# def sequence_sum(start, end, step):
#     return sum(range(start, end+1, step))


def fixed_tests():
    assert sequence_sum(2, 6, 2) == 12
    assert sequence_sum(1, 5, 1) == 15
    assert sequence_sum(1, 5, 3) == 5
    assert sequence_sum(0, 15, 3) == 45
    assert sequence_sum(16, 15, 3) == 0
    assert sequence_sum(2, 24, 22) == 26
    assert sequence_sum(2, 2, 2) == 2
    assert sequence_sum(2, 2, 1) == 2
    assert sequence_sum(1, 15, 3) == 35
    assert sequence_sum(15, 1, 3) == 0


begin_number, end_number, step = 2, 6, 2
qq(sequence_sum(begin_number, end_number, step))
fixed_tests()

end = timer()
print(end - start)
