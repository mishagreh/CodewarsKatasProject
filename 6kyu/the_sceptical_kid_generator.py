from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/570957fc20a35bd2df0004f9

def alan_annoying_kid(sentence: str) -> str:
    """ returns the kid's reply """

    s = sentence.split()
    pos = sentence.partition(s[2])
    neg = sentence.partition(s[3])

    if s[2][-2:] == 'ed':
        return f"I don't think you {s[2]}{pos[-1][:-1]} today, I think you didn't {s[2][:-2]} at all!"
    return f"I don't think you didn't {s[3]}{neg[-1][:-1]} today, I think you did {s[3]} it!"


sentence = "Today I didn't attempt to hardcode this Kata."
print(alan_annoying_kid(sentence))

end = timer()
print(end - start)
