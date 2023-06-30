from timeit import default_timer as timer

start = timer()
qq = print


def to_industrial(time):
    return round(time/60, 2) if isinstance(time, int) else round(int(time[-2:])/60, 2) + int(time[:-3])


def to_normal(time):
    x = round(time*100)
    return '{}:{:02d}'.format(x*36//3600, round((x*36 % 3600)/60))


end = timer()
print(end - start)
