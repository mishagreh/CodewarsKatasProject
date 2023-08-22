from timeit import default_timer as timer

start = timer()
qq = print

# https://www.codewars.com/kata/559536379512a64472000053

import string


def play_pass(s: str, n: int) -> str:
    """ returns encoded input string  """

    alpha = string.ascii_uppercase
    before = alpha + ''.join(tuple(map(str, (range(10)))))
    after = alpha[n:] + alpha[:n] + ''.join(tuple(map(str, reversed(range(10)))))
    s = s.translate(s.maketrans(before, after))

    return ''.join([j.lower() if j.isalpha() and k % 2 else j for k, j in enumerate(s)])[::-1]


s, n = "MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2
print(play_pass(s, n))

end = timer()
print(end - start)
