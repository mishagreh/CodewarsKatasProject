from timeit import default_timer as timer

start = timer()
qq = print


# Given an integer n and two other values, build an array of size n filled with these two values alternating.
#
# Examples
# 5, true, false     -->  [true, false, true, false, true]
# 10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
# 0, "one", "two"    -->  []


def alternate(n, first_value, second_value):
    """ returns an array of size n filled with two values alternating """

    return [first_value if i%2 == 0 else second_value for i in range(n)]


def tests():
    assert alternate(5, True, False) == [True, False, True, False, True]
    assert alternate(20, "blue", "red") == \
           ['blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red',
                        'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red']
    assert alternate(0, "lemons", "apples") == []


n, first_value, second_value = 20, "blue", "red"
qq(alternate(n, first_value, second_value))
tests()

end = timer()
print(end - start)
