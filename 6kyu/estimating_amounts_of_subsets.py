from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/584703d76f6cf6ffc6000275

def est_subsets(arr):
    return 2**len(arr)-1


arr = [1, 2, 3, 4]
print(est_subsets(arr))

end = timer()
print(end - start)
