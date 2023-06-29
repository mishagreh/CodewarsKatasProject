from timeit import default_timer as timer
import re

start = timer()
qq = print


def consonant_count(s):
    """
    The function that takes a string of English-language text and returns the number of consonants in the string.
    """

    return len(re.findall('[bcdfghjklmnpqrstvwxz]', s.lower()))


s = 'h^$&^#$&^elLo world'
qq(consonant_count(s))

end = timer()
print(end - start)
