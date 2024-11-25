# Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
# Intervals
#
# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5. The length of this
# interval is 4.
def foo(x, y):
    return min(x[0], y[0]), max(x[1], y[1])


def sorting(intervals, sorted_values, res):
    if intervals == []:
        # return sorted_values
        return res
    x = f'{intervals[0]}'
    # print(intervals)
    sorted_values[x] = intervals[0]
    # print(sorted_values)
    intervals.remove(intervals[0])
    # print(intervals)
    # print(intervals == [])

    if intervals == []:
        res += subt(sorted_values[x])
        # print(sorted_values[x])
        # print(res)
        # return sorted_values
        return res

    else:
        q = iter(intervals)
        while True:
            try:
                z = next(q)
                # print(z)
                # # if int(y[0][1]) <= (intervals[0][0]) <= int(y[0][-2]):
                # print(sorted_values[x][0])
                # print(sorted_values[x][0])
                # print(z[0])
                # print(sorted_values[x][1])
                if sorted_values[x][0] <= z[0] <= sorted_values[x][1] or \
                        sorted_values[x][0] <= z[1] <= sorted_values[x][1]:
                    a = list(map(foo, [sorted_values[x]], [z]))[0]
                    sorted_values[x] = a
                    intervals.remove(z)
                    # print(intervals, sorted_values)
                # break
                continue
            except StopIteration:
                res += subt(sorted_values[x])
                # print(sorted_values)
                # print(res)
                return sorting(intervals, sorted_values, res)

        # return sorting(intervals, sorted_values)


def subt(x):
    return x[1]-x[0]


def sum_of_intervals(intervals):
    sorted_values = {}
    res = 0
    res = sorting(intervals, sorted_values, res)

    # return sum(map(subt, sorting(intervals, sorted_values).values()))
    # return sum(sorting(intervals, sorted_values).values())
    return res


if __name__ == '__main__':
    print(sum_of_intervals([(1, 5), (1, 5)]))
# test.assert_equals(sum_of_intervals([(1, 5)]), 4)
# test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
# test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
# test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
