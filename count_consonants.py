from timeit import default_timer as timer
import re

start = timer()
qq = print

def consonant_count(s):
    """
    The func takes a str of English-language text and returns
    the number of consonants in it
    """

    return len(re.findall("[bcdfghjklmnpqrstvwxyz]", s.lower()))

s = "h!@#$%^elLo World"
qq(consonant_count(s))

end = timer()
print(end - start)
