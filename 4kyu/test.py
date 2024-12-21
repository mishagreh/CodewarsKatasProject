def longest_slide_down(p):
    res = p.pop()
    print(res)
    while p:
        tmp = p.pop()
        print(tmp)
        res = [tmp[i] + max(res[i], res[i+1]) for i in range(len(tmp))]
        print(res)
    return res.pop()


pyr = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
print(longest_slide_down(pyr))
