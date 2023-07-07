from timeit import default_timer as timer

start = timer()
qq = print

#  https://www.codewars.com/kata/5b1b27c8f60e99a467000041/train/python


def anagram_difference(w1, w2):
    """
        :return: the number of characters to remove from w1 and w2 to make them anagrams of each other
    """

    #  1) return a number (count1) of chars not matching wittingly
    #  2) return a number (count2) of extra chars

    ww = [''.join(c for c in i if c in set(w1).intersection(set(w2))) for i in (w1, w2)]
    count1 = len(w1 + w2) - len(''.join(ww))

    extra = [[i.count(c) for c in set(ww[0])] for i in ww]
    count2 = sum(list(abs(extra[0][i] - extra[1][i]) for i, c in enumerate(extra[0])))

    return count1 + count2


# def tests():


w1, w2 = ['b', 'z', 'y', 'n', 'n', 'l', 'd', 'd', 'k', 's', 'r', 't', 'a', 'b', 'a', 'f'], ['z', 'c', 'u', 'v', 'h', 'l', 'u', 'z', 's', 'f', 'l', 'v', 'w', 'v', 'p', 'm', 'v', 'j', 'c', 'm', 'g', 'f', 'b', 'j', 'q', 'v', 'z', 'q', 'd', 'f', 'y', 'x', 'x', 'd', 'g', 'x', 'l']  # ['m', 'm', 'c', 'i', 's', 'b', 'b'], ['a', 'c', 'b', 'p', 'i', 'o', 'p', 'b'] # 'aab', 'a' #
qq(anagram_difference(w1, w2))
# tests()


end = timer()
print(end - start)

