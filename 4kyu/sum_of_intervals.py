# Write a function called sumIntervals/sum_intervals that accepts an array
# of intervals, and returns the sum of all the interval lengths.
# Overlapping intervals should only be counted once.
#
# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5. The length of this
# interval is 4.
#
# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals, result=0):
    """ Recursive function, that accepts an array of intervals,
        and returns the sum of all the interval lengths. """

    if intervals != []:
        buffer = intervals[0]
        iterator = iter(intervals)
        while True:
            try:
                item = next(iterator)
                condition1 = buffer[0] <= item[0] <= buffer[1] or \
                    buffer[0] <= item[1] <= buffer[1]
                condition2 = item[0] <= buffer[0] and \
                    buffer[1] <= item[1]
                if condition1 or condition2:
                    buffer = (
                            min(buffer[0], item[0]),
                            max(buffer[1], item[1])
                    )
                    intervals.remove(item)
                    iterator = iter(intervals)
                continue
            except StopIteration:
                result += buffer[1] - buffer[0]
                return sum_of_intervals(intervals, result)

    return result


if __name__ == '__main__':
    print(sum_of_intervals([(217, 225), (-209, 436), (-117, 385)]))
# test.assert_equals(sum_of_intervals([(1, 5)]), 4)
# test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
# test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
# test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
