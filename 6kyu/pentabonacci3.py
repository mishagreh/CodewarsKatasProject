from functools import cache



def pentaFib(n, memo):
    """ returns the last number + all numbers dictionary """

    f = count_odd_pentaFib

    match n:
        case 0: return 0
        case 1: return 1
        case 2: return 1
        case 3: return 2
        case 4: return 4

    return pentaFib.ca
@cache
def count_odd_pentaFib(n):
    """ counts the odd numbers in the all numbers dictionary """

    f = count_odd_pentaFib

    match n:
        case 0: return 0
        case 1: return 1
        case 2: return 1
        case 3: return 2
        case 4: return 4

    return f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4) + f(n - 5)


n = 30
print(count_odd_pentaFib(n))