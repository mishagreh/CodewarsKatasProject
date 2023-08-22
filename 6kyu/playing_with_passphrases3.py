from timeit import default_timer as timer
from string import digits, ascii_uppercase as auc

start = timer()
qq = print

# https://www.codewars.com/kata/559536379512a64472000053


def play_pass(s: str, n: int) -> str:
    """ returns encoded input string  """

    s = s.translate(s.maketrans(auc + digits, auc[n:] + auc[:n] + digits[::-1]))

    return ''.join([j.lower() if j.isalpha() and i % 2 else j for i, j in enumerate(s)])[::-1]


s, n = "MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2
print(play_pass(s, n))

end = timer()
print(end - start)
