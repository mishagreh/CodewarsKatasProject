from timeit import default_timer as timer
import math

start = timer()
qq = print

#  https://www.codewars.com/kata/58ae6ae22c3aaafc58000079


def permute_a_palindrome(input):
    """ returns if the input can be a palindrome (True/False) """

    if len(input)%2 == 0:
        for i in set(input):
            if input.count(i)%2 != 0:
                return False
        # return True
    odd = 0
    for i in set(input):
        if input.count(i)%2 == 0:
            continue
        odd += 1
        if odd == 2:
            return False
    return True

    # + several clever solutions


    # return sum(input.count(c) % 2 for c in set(input)) < 2


    # flag = 0
    # for i in set(input):
    #     if input.count(i) % 2 == 1:
    #         flag += 1
    # return flag < 2


    # return sum(stg.count(c) % 2 for c in set(stg)) == len(stg) % 2


# def tests():

input = 'abcccccba'
permute_a_palindrome(input)


# tests()


end = timer()
print(end - start)
