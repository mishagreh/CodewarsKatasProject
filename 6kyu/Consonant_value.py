from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/59c633e7dcc4053512000073


def solve(string):
    """ returns sum2 counter of the longest consonant series. Sum1 is an intermediary counter """

    dict = {'b': 2, 'c': 3, 'd': 4, 'f': 6, 'g': 7, 'h': 8, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'p': 16,
            'q': 17, 'r': 18, 's': 19, 't': 20, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    sum1 = 0
    sum2 = 0

    for i in string:
        if i not in "aeiou":
            sum1 += dict[i]
        else:
            if sum1 > sum2:
                sum2 = sum1
            sum1 = 0
    if sum1 > sum2:
        sum2, sum1 = sum1, 0

    return sum2


def tests():
    assert solve("cozy") == 51
    assert solve("xyzzy") == 126
    assert solve("zodiac") == 26
    assert solve("chruschtschov") == 80
    assert solve("khrushchev") == 38
    assert solve("strength") == 57
    assert solve("catchphrase") == 73
    assert solve("twelfthstreet") == 103
    assert solve("mischtschenkoana") == 80


string = "sasasachruschtschova"
qq(solve(string))
tests()

end = timer()
print(end - start)
