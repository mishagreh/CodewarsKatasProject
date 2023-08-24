from timeit import default_timer as timer
from string import ascii_uppercase as auc

start = timer()
qq = print


# https://www.codewars.com/kata/529b418d533b76924600085d/

def to_underscore(s: str) -> str:
    """ converts from CamelCase to snake_case """

    if type(s) == int:
        return str(s)

    uppers = [i for i, j in enumerate(s) if j in auc] + [len(s)]
    substrings = [s[uppers[i]:uppers[i + 1]] for i in range(len(uppers) - 1)]

    return '_'.join(substrings).lower()


# short solution
#
# def to_underscore(s):
#     return "".join(["_" + c.lower() if c.isupper() else c for c in str(s)]).strip("_")

s = "App7Test"
print(to_underscore(s))


end = timer()
print(end - start)
