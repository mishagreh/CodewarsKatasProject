from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/64348795d4d3ea00196f5e76

def binary_average(binary):
    if len(binary) > 1 and binary[0] == 'x':
        binary = '1' + binary[1:]

    min_num = int(binary.replace('x', '0'), 2)
    max_num = int(binary.replace('x', '1'), 2)

    return (min_num + max_num) / 2


binary = 'xx'
print(binary_average(binary))

end = timer()
print(end - start)
