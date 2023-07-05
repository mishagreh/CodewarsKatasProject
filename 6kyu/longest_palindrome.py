from timeit import default_timer as timer
from itertools import zip_longest

start = timer()
qq = print

#  https://www.codewars.com/kata/54bb6f887e5a80180900046b


def longest_palindrome(s):
    """ finding palidromes starting with each letter and returns the longest palindrome length """

    winner = ''
    for i, c in enumerate(s):
        candidate = ''
        for char in s[i:]:
            candidate += char
            if candidate == candidate[::-1] and len(candidate) >= len(winner):
                winner = candidate
    return 0 if s == '' else len(winner)


def tests():
    assert longest_palindrome("a") == 1
    assert longest_palindrome("aa") == 2
    assert longest_palindrome("baa") == 2
    assert longest_palindrome("aab") == 2
    assert longest_palindrome("abcdefghba") == 1
    assert longest_palindrome("baablkj12345432133d") == 9
    assert longest_palindrome("") == 0


s = "abcdefghijklmnopqrstuvwxyzlolollolollolollolol"

qq(longest_palindrome(s))
tests()

end = timer()
print(end - start)