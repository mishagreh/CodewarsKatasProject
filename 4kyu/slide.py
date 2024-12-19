# https://www.codewars.com/kata/551f23362ff852e2ab000037
#
#    /3/
#   \7\ 4
#  2 \4\ 6
# 8 5 \9\ 3
#
# longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]), 23
from itertools import cycle
from pprint import pprint
import pdb


def recur(pyr: list, coords: list, level):
    print(' ')
    print('coords:', coords)
    print('sorted coords:', sorted(coords))
    res = []
    # for item in range(len(coords)//2):
    for item in range(0, len(coords), 2):
        print('item:', item)
        x = coords[item][level-1]
        # print(x)
        y = level-1
        # print(y)
        print(pyr[y][x], pyr[y][x+1])
        if pyr[y][x] < pyr[y][x+1]:
            # coords.pop(item)
            res.append(coords[item+1])
        elif pyr[y][x] > pyr[y][x+1]:
            # coords.pop(item+1)
            res.append(coords[item])
    # print(coords)
    # print('len coords:', len(coords))
    if len(res) == 1:
        # print('ghjghj')
        # print(coords)
        return res[0]
    else:
        return recur(pyr, res, level-1)


def longest_slide_down(pyr):
    # x = 0000, y = 0123
    # x = 0001, y = 0123
    #
    # x = 0011, y = 0123
    # x = 0012, y = 0123
    #
    # x = 0111, y = 0123
    # x = 0112, y = 0123
    #
    # x = 0122, y = 0123
    # x = 0123, y = 0123
    #
    # 0000x
    # 0001x
    # 0011x
    # 0012x
    #
    y = range(len(pyr))
    zz = [0 for i in range(len(pyr)-1)]
    qq = [zz]
    # print('len(pyr):', len(pyr))
    aa = zip(range(pow(2, len(pyr)-2)-1), cycle(range(len(pyr)-2, 0, -1)))
    aa = list(aa)
    print(aa)
    for i, j in aa:
        ww = qq[-1].copy()
        # print('i:', i)
        # for j in range():
        # print('j:', j)
        if ww[j] < j:
            ww[j] += 1
            qq.append(ww)
            # print(ww)
            # pprint(qq)
    print('qq:', qq)
    ss = []
    # breakpoint()
    for li in qq:
        for ji in (0, 1):
            k = li.copy()
            k.append(li[-1]+ji)
            ss.append(k)
    print('ss:', ss)
    # ss = list(filter(lambda i: ))
    level = len(pyr)
    eee = recur(pyr, ss, level)
    print('result:', eee)
    summa = 0
    for i in list(zip(y, eee)):
        summa += pyr[i[0]][i[1]]
    return summa


pyr = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 100]]
# pyr = [[3], [7, 4], [2, 4, 6]]
# pyr = [[3], [7, 4]]
# print(longest_slide_down(pyr))

# pyr = [
#             [75],
#             [95, 64],
#             [17, 47, 82],
#             [18, 35, 87, 10],
            # [20,  4, 82, 47, 65],
            # [19,  1, 23, 75,  3, 34],
            # [88,  2, 77, 73,  7, 63, 67],
            # [99, 65,  4, 28,  6, 16, 70, 92],
            # [41, 41, 26, 56, 83, 40, 80, 70, 33],
            # [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            # [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            # [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            # [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            # [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            # [4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            # ]

print(longest_slide_down(pyr))
