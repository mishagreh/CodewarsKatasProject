from timeit import default_timer as timer
from collections import Counter as c

start = timer()
qq = print


# https://www.codewars.com/kata/5971b219d5db74843a000052

def added_char(s1, s2):
    cnt1, cnt2 = c(s1), c(s2)
    cnt2.subtract(cnt1)
    return tuple(cnt2.elements())[0]


s1, s2 = "aabbcc", "aacccbbcc"
print(added_char(s1, s2))

end = timer()
print(end - start)
