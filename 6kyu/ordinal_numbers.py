from timeit import default_timer as timer
from collections import Counter as c

start = timer()
qq = print


# https://www.codewars.com/kata/52dda52d4a88b5708f000024


def ordinal(number: int, brief: bool = False) -> str:
    """ returns an appropriate ordinal suffix """

    last_two = str(number)[-2:]
    last_one = str(number)[-1]

    if last_one in ('1', '2', '3'):

        match last_two:
            case '11' | '12' | '13':
                return 'th'

        match last_one, brief:
            case '1', True | 1 | False | 0:
                return 'st'
            case '2', False | 0:
                return 'nd'
            case '2' | '3', True | 1:
                return 'd'
            case '3', False | 0:
                return 'rd'

    return 'th'


number, brief = 417891, 1
print(ordinal(number, brief))

end = timer()
print(end - start)
