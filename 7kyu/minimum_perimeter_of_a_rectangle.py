from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/5826f54cc60c7e5266000baf


def minimum_perimeter(area):
    """ given an area as a positive integer, returns the smallest perimeter possible """

    side = [i for i in range(1, int((area**0.5) + 1)) if not area % i][-1]
    return 2*int(side + area/side)


area = 45
qq(minimum_perimeter(area))
# tests()


end = timer()
print(end - start)
