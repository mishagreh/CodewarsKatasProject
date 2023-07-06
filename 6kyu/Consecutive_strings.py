from timeit import default_timer as timer
import itertools

start = timer()
qq = print

# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python


def longest_consec(strarr, k):
    """  returns the first longest string consisting of k consecutive strings taken in the array """

    if k <= 0 or strarr == [] or k > len(strarr):
        return ''
    return max([''.join(strarr[i:i+k]) for i in range(len(strarr))], key=len)

    # if k <= 0 or strarr == [] or k > len(strarr):
    #     return ''
    # a = [strarr[i:i+k] for i in range(len(strarr))]
    # return max([''.join(j) for j in a], key=len)

    # don't understand why it can't catch k = -2 ValueError
    # try:
    #     a = [strarr[i:i+k] for i in range(len(strarr))]
    #     return max([''.join(j) for j in a], key=len)
    # except ValueError:
    #     return ''



def tests():
    assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"
    assert longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)\
           == "oocccffuucccjjjkkkjyyyeehh"
    assert longest_consec([], 3) == ""
    assert longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"],
                          2) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
    assert longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2)\
           == "wlwsasphmxxowiaxujylentrklctozmymu"
    assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) == ""
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz"
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15) == ""
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0) == ""


strarr, k = ["zone", "abigail", "theta", "form", "libe", "zas"], 2
qq(longest_consec(strarr, k))
tests()

end = timer()
print(end - start)