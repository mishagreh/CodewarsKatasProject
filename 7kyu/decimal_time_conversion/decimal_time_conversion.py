from timeit import default_timer as timer

start = timer()
qq = print


def to_industrial(time):
    """
    Accepts either the time in minutes as an integer or a string of the format "h:mm".
    Returns a float that represents decimal hours (e.g. 1.75 for 1h 45m).
    """

    return round(time/60, 2) if isinstance(time, int) else round(int(time[-2:])/60, 2) + int(time[:-3])


def to_normal(time):
    """
    Accepts a float representing decimal time in hours.
    Returns a string that represents standard time in the format "h:mm".
    """

    x = round(time*3600)
    return '{}:{:02d}'.format(int(time), round(x % 3600/60))


end = timer()
print(end - start)