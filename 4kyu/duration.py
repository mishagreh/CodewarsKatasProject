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
import pdb


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    years = divmod(seconds, 24*3600*365)
    days = divmod(years[1], 24*3600)
    hours = divmod(days[1], 3600)
    mins = divmod(hours[1], 60)
    secs = mins[1], 'placeholder'
    words = 'year', 'day', 'hour', 'minute', 'second'
    # breakpoint()
    output = []
    for num, dur in enumerate((years, days, hours, mins, secs)):
        if dur[0] != 0:
            output.append(
                f'{dur[0]}' + (f' {words[num]}' if dur[0] == 1 else f' {words[num]}s')
            )
    # print(output)
    if len(output) > 1:
        return ', '.join(output[:-1]) + ' and ' + output[-1]
    else:
        return output[-1]


print(format_duration(0))
