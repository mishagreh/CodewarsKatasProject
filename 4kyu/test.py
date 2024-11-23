from datetime import datetime


def decor(f):
    def wrapper(*args):
        start = datetime.now()
        f(*args)
        end = datetime.now()
        duration = end - start
        print(duration)
    return wrapper


@decor
def plus(x, y):
    print(str(int(x) + int(y)))


@decor
def dic(x, y):
    d = {'12': '3'}
    print(d[x+y])


plus('1', '2')
dic('1', '2')
