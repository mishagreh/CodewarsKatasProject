from timeit import default_timer as timer

start = timer()
qq = print

# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
# neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.


def disemvowel(string_):
    """ takes a string and returns a new string with all vowels removed. """

    for i in string_:
        if i in 'aeiouAEIOU':
            string_ = string_.replace(i, '')
    return string_


# a couple of short solutions
# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")

# def disemvowel(s):
#     for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#     return s



string_ = "This website is for losers LOL!"
qq(disemvowel(string_))
# fixed_tests()

end = timer()
print(end - start)
