# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
#
# ('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']),
# 'apples, pears\ngrapes\nbananas')
# ('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
# (' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')

def strip_comments(string, markers):
    x = string.split('\n')
    for marker in markers:
        x = list(map(
            lambda i: i.partition(f'{marker}')[0].rstrip(), x
        ))
    return '\n'.join(x)


# print(ord('\n'))
string = '?\nlemons\n. bananas lemons apples cherries'
markers = ['#', '=', '.', '^', '!', '@', '-']
# '?\nlemons\n. bananas lemons apples cherries' should equal '?\nlemons\n'
# print(string)
# for i in string:
    # print(i, 'qq')

pp = '# 123'
# print(pp.partition('#'))
strip_comments(string, markers)
