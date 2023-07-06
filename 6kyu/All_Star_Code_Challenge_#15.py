from timeit import default_timer as timer

start = timer()
qq = print

#  https://www.codewars.com/kata/586560a639c5ab3a260000f3/train/python


def rotate(str_):
    """ returns an array of strings with each letter from the input string being rotated to the end (4 options) """

    return [str_[i+1:] + str_[:i+1] for i in range(len(str_))]


    # return [str_[i:] + str_[:i] for i in range(1, len(str_) + 1)]

    # rotate = lambda str_: [str_[i + 1:] + str_[:i + 1] for i in range(len(str_))]

    # res = []
    # for i in range(len(str_)):
    #     str_ = str_[1:] + str_[0]
    #     res.append(str_)
    # return res


def tests():
    assert rotate("Hello") == ["elloH", "lloHe", "loHel", "oHell", "Hello"]
    assert rotate(" ") == [" "]
    assert rotate("") == []
    assert rotate("123") == ["231", "312", "123"]


str_ = ' '
qq(rotate(str_))
tests()

end = timer()
print(end - start)