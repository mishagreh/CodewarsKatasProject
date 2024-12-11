# https://www.codewars.com/kata/563f879ecbb8fcab31000041
#

def factory(number):
    def item(array):
        # return list(map(lambda element: element*number, array))
        return [element*number for element in array]
    return item


fives = factory(5)
array = [1, 2, 3]
print(fives(array))
