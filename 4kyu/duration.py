# https://www.codewars.com/kata/52742f58faf5485cae000b9a
# (0), "now")
# (1), "1 second")
# (62), "1 minute and 2 seconds")
# (120), "2 minutes")
# (3600), "1 hour")
# (3662), "1 hour, 1 minute and 2 seconds")
# (15731080), "182 days, 1 hour, 44 minutes and 40 seconds")
# (132030240), "4 years, 68 days, 3 hours and 4 minutes")
# (205851834), "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
# (253374061), "8 years, 12 days, 13 hours, 41 minutes and 1 second")
# (242062374), "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
# (101956166), "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
# (33243586), "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")
from itertools import accumulate
from operator import mul


def format_duration(seconds):
    if not seconds:
        return 'now'

    numer = seconds
    denoms = list(accumulate([1, 60, 60, 24, 365], mul))[::-1]
    words = 'year', 'day', 'hour', 'minute', 'second'
    numbers = []
    for i in range(5):
        x, y = divmod(numer, denoms[i])
        numbers.append((x, words[i]))
        numer = y

    output = []
    for number, word in numbers:
        if number:
            output.append(
                f'{number}' + (f' {word}' if number == 1 else f' {word}s')
            )
    if len(output) > 1:
        return ', '.join(output[:-1]) + ' and ' + output[-1]
    else:
        return output[0]


print(format_duration(86404))
