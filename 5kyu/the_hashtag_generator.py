from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s: str) -> str:
    """ returns a hashtagged string """

    s1 = '#' + s.title().replace(' ', '')

    if 1 < len(s1) <= 140:
        return s1
    return False


s = 'Codewars Is Nice'
print(generate_hashtag(s))

end = timer()
print(end - start)
