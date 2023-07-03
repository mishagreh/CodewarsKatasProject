from timeit import default_timer as timer

start = timer()
qq = print

# https://www.codewars.com/kata/6498aa0daff4420024ce2c88

def get_in_line(arr: list[int]) -> int:
    

def tests():
    assert get_in_line([1, 1, 3, 2, 0]) == 3
    assert get_in_line([0, 8, 2, 1, 4, 2, 12, 3, 2]) == 6


@test.it("More Tests")
def more_tests():
    assert get_in_line([2, 3, 1, 4, 5, 2, 1, 0, 8, 5, 6, 1]) == 10
    assert get_in_line([12, 3, 19, 14, 1, 19, 16, 4, 0, 1]) == 3
    assert get_in_line([13, 20, 3, 3, 14, 5, 13, 0, 8, 5]) == 8
    assert get_in_line([16, 4, 3, 0, 1, 3, 7, 3, 10, 1]) == 6
    assert get_in_line([1, 1, 1, 3, 3, 8, 3, 14, 3, 0]) == 10
    assert get_in_line([0]) == 1


arr = [1, 1, 1, 3, 3, 8, 3, 14, 3, 0]
qq(get_in_line(arr))
tests()

end = timer()
print(end - start)
