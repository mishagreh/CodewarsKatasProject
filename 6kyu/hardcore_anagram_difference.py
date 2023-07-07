from timeit import default_timer as timer
import math

start = timer()
qq = print

#  https://www.codewars.com/kata/5b1b48cc647c7e7c56000083


def anagram_difference(words):
    """
        :return: the number of characters to remove from the words to make them anagrams of each other
    """
    # x = total number of letters in words. y = total number of letters in anagrams

    letters_per_word = [[i.count(j) for j in set(''.join(words))] for i in words]

    x = sum(len(i) for i in words)

    y = sum(min(i)*len(words) for i in zip(*letters_per_word) if math.prod(i))

    return x - y


# def tests():


words = {'allo', 'hola', 'hello'}
qq(anagram_difference(words))
# tests()


end = timer()
print(end - start)
