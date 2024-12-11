# https://www.codewars.com/kata/598106cb34e205e074000031
#
#

def count_rats(input):
    input = input.replace(' ', '')
    l, P, r = input.partition('P')
    lr = []
    for i in l, r:
        lr.append([i[x:x+2] for x in range(0, len(i), 2)])

    return lr[0].count('O~') + lr[1].count('~O')


input = '~O ~O~O~OP~O~O O~'
print(count_rats(input))
