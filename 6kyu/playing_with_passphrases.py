from timeit import default_timer as timer
import string

start = timer()
qq = print


# https://www.codewars.com/kata/559536379512a64472000053

import string


def play_pass(s, n):
    alpha = string.ascii_uppercase

    for k, j in enumerate(s):
        if j.isalpha():
            if alpha.index(j) + n > 25:
                s = s[:k] + alpha[alpha.index(j) + n - 26] + s[k + 1:]
            else:
                s = s[:k] + alpha[alpha.index(j) + n] + s[k + 1:]
        elif j.isdigit():
            s = s[:k] + str(9 - int(j)) + s[k + 1:]

    for k, j in enumerate(s):
        if k % 2:
            s = s[:k] + j.lower() + s[k + 1:]

    return s[::-1]


s, n = "MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2
print(play_pass(s, n))


end = timer()
print(end - start)
