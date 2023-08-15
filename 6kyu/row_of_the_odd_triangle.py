from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/5d5a7525207a674b71aa25b5

def odd_row(n):
    """ returns the n-th row of the given odd numbers triangle  """

    last_el = 1
    row_step = 4
    for i in range(n - 1):
        last_el += row_step
        row_step += 2

    return [i for i in range(last_el - row_step + 4, last_el + 2, 2)]


n = 2
print(odd_row(n))

end = timer()
print(end - start)
