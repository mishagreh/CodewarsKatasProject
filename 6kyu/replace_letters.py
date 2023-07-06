from timeit import default_timer as timer
import itertools

start = timer()
qq = print

#  https://www.codewars.com/kata/5a4331b18f27f2b31f000085


def replace_letters(word):
    """
        replace the vowel with the nearest left consonant.
        replace the consonant with the nearest right vowel.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    translate = {}
    j = 0

    for i, char in enumerate(alphabet):
        if char in vowels:
            translate[char] = alphabet[i - 1]
            j += 1
        else:
            translate[char] = vowels[j]
            if j == len(vowels) - 1:
                j = -1

    return ''.join(translate[char] for char in word)


# def tests():

word = 'codewars'
qq(replace_letters(word))
# tests()

end = timer()
print(end - start)