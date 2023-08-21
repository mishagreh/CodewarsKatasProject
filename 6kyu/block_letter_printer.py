from timeit import default_timer as timer
import string

start = timer()
qq = print


# https://www.codewars.com/kata/6375587af84854823ccd0e90

# Write a program that accepts a string in ASCII letters and the whitespace,
# and then returns that string in block letters of 5 spaces/signs width and
# 7 spaces/signs height. The block letters shall consist of corresponding
# capital letters.
# The string should be formatted in a way that when passed to the print()
# function shows the desired output.

def alphabet_dict(s1: str) -> dict:
    alphabet_list = s1.splitlines()[1:]
    alpha = {}

    for i in range(2, 6):
        alphabet_list[i] += (i - 1) * ' '
    for i in range(7):
        alphabet_list[i] += ' '

    s3 = string.ascii_uppercase

    for i in s3:
        alpha[i] = {}
        for j in range(7):
            alpha[i][j] = alphabet_list[j][6 * s3.index(i):6 * (s3.index(i) + 1)]

    alpha[' '] = {}
    for i in range(7):
        alpha[' '][i] = '      '

    return alpha


def block_print(s: str) -> str:
    """ returns a string with letters made by letters (i.e. so-called block letters) """

    alpha = {'A': {0: ' AAA  ', 1: 'A   A ', 2: 'A   A ', 3: 'AAAAA ', 4: 'A   A ', 5: 'A   A ', 6: 'A   A '},
             'B': {0: 'BBBB  ', 1: 'B   B ', 2: 'B   B ', 3: 'BBBB  ', 4: 'B   B ', 5: 'B   B ', 6: 'BBBB  '},
             'C': {0: ' CCC  ', 1: 'C   C ', 2: 'C     ', 3: 'C     ', 4: 'C     ', 5: 'C   C ', 6: ' CCC  '},
             'D': {0: 'DDDD  ', 1: 'D   D ', 2: 'D   D ', 3: 'D   D ', 4: 'D   D ', 5: 'D   D ', 6: 'DDDD  '},
             'E': {0: 'EEEEE ', 1: 'E     ', 2: 'E     ', 3: 'EEEEE ', 4: 'E     ', 5: 'E     ', 6: 'EEEEE '},
             'F': {0: 'FFFFF ', 1: 'F     ', 2: 'F     ', 3: 'FFFFF ', 4: 'F     ', 5: 'F     ', 6: 'F     '},
             'G': {0: ' GGG  ', 1: 'G   G ', 2: 'G     ', 3: 'G GGG ', 4: 'G   G ', 5: 'G   G ', 6: ' GGG  '},
             'H': {0: 'H   H ', 1: 'H   H ', 2: 'H   H ', 3: 'HHHHH ', 4: 'H   H ', 5: 'H   H ', 6: 'H   H '},
             'I': {0: 'IIIII ', 1: '  I   ', 2: '  I   ', 3: '  I   ', 4: '  I   ', 5: '  I   ', 6: 'IIIII '},
             'J': {0: 'JJJJJ ', 1: '    J ', 2: '    J ', 3: '    J ', 4: '    J ', 5: '    J ', 6: 'JJJJ  '},
             'K': {0: 'K   K ', 1: 'K  K  ', 2: 'K K   ', 3: 'KK    ', 4: 'K K   ', 5: 'K  K  ', 6: 'K   K '},
             'L': {0: 'L     ', 1: 'L     ', 2: 'L     ', 3: 'L     ', 4: 'L     ', 5: 'L     ', 6: 'LLLLL '},
             'M': {0: 'M   M ', 1: 'MM MM ', 2: 'M M M ', 3: 'M   M ', 4: 'M   M ', 5: 'M   M ', 6: 'M   M '},
             'N': {0: 'N   N ', 1: 'NN  N ', 2: 'N   N ', 3: 'N N N ', 4: 'N   N ', 5: 'N  NN ', 6: 'N   N '},
             'O': {0: ' OOO  ', 1: 'O   O ', 2: 'O   O ', 3: 'O   O ', 4: 'O   O ', 5: 'O   O ', 6: ' OOO  '},
             'P': {0: 'PPPP  ', 1: 'P   P ', 2: 'P   P ', 3: 'PPPP  ', 4: 'P     ', 5: 'P     ', 6: 'P     '},
             'Q': {0: ' QQQ  ', 1: 'Q   Q ', 2: 'Q   Q ', 3: 'Q   Q ', 4: 'Q Q Q ', 5: 'Q  QQ ', 6: ' QQQQ '},
             'R': {0: 'RRRR  ', 1: 'R   R ', 2: 'R   R ', 3: 'RRRR  ', 4: 'R R   ', 5: 'R  R  ', 6: 'R   R '},
             'S': {0: ' SSS  ', 1: 'S   S ', 2: 'S     ', 3: ' SSS  ', 4: '    S ', 5: 'S   S ', 6: ' SSS  '},
             'T': {0: 'TTTTT ', 1: '  T   ', 2: '  T   ', 3: '  T   ', 4: '  T   ', 5: '  T   ', 6: '  T   '},
             'U': {0: 'U   U ', 1: 'U   U ', 2: 'U   U ', 3: 'U   U ', 4: 'U   U ', 5: 'U   U ', 6: ' UUU  '},
             'V': {0: 'V   V ', 1: 'V   V ', 2: 'V   V ', 3: 'V   V ', 4: 'V   V ', 5: ' V V  ', 6: '  V   '},
             'W': {0: 'W   W ', 1: 'W   W ', 2: 'W   W ', 3: 'W W W ', 4: 'W W W ', 5: 'W W W ', 6: ' W W  '},
             'X': {0: 'X   X ', 1: 'X   X ', 2: ' X X  ', 3: '  X   ', 4: ' X X  ', 5: 'X   X ', 6: 'X   X '},
             'Y': {0: 'Y   Y ', 1: 'Y   Y ', 2: ' Y Y  ', 3: '  Y   ', 4: '  Y   ', 5: '  Y   ', 6: '  Y   '},
             'Z': {0: 'ZZZZZ ', 1: '    Z ', 2: '   Z  ', 3: '  Z   ', 4: ' Z    ', 5: 'Z     ', 6: 'ZZZZZ '},
             ' ': {0: '      ', 1: '      ', 2: '      ', 3: '      ', 4: '      ', 5: '      ', 6: '      '}}

    res = ''
    for i in range(7):
        for k, j in enumerate(s.upper().strip()):
            res += alpha[j][i]
        res = res.rstrip() + '\n'

    return res[:-1]


s = '   but   different   '

s1 = '''
 AAA  BBBB   CCC  DDDD  EEEEE FFFFF  GGG  H   H IIIII JJJJJ K   K L     M   M N   N  OOO  PPPP   QQQ  RRRR   SSS  TTTTT U   U V   V W   W X   X Y   Y ZZZZZ
A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     MM MM NN  N O   O P   P Q   Q R   R S   S   T   U   U V   V W   W X   X Y   Y     Z
A   A B   B C     D   D E     F     G     H   H   I       J K K   L     M M M N   N O   O P   P Q   Q R   R S       T   U   U V   V W   W  X X   Y Y     Z
AAAAA BBBB  C     D   D EEEEE FFFFF G GGG HHHHH   I       J KK    L     M   M N N N O   O PPPP  Q   Q RRRR   SSS    T   U   U V   V W W W   X     Y     Z
A   A B   B C     D   D E     F     G   G H   H   I       J K K   L     M   M N   N O   O P     Q Q Q R R       S   T   U   U V   V W W W  X X    Y    Z
A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     M   M N  NN O   O P     Q  QQ R  R  S   S   T   U   U  V V  W W W X   X   Y   Z
A   A BBBB   CCC  DDDD  EEEEE F      GGG  H   H IIIII JJJJ  K   K LLLLL M   M N   N  OOO  P      QQQQ R   R  SSS    T    UUU    V    W W  X   X   Y   ZZZZZ'''

print(alphabet_dict(s1))

print(block_print(s))

print('BBBB  U   U TTTTT                   DDDD  IIIII FFFFF FFFFF EEEEE RRRR  EEEEE N   N TTTTT\nB   B U   U   T'
      '                     D   D   I   F     F     E     R   R E     NN  N   T\nB   B U   U   T                 '
      '    D   D   I   F     F     E     R   R E     N   N   T\nBBBB  U   U   T                     D   D   I   F'
      'FFFF FFFFF EEEEE RRRR  EEEEE N N N   T\nB   B U   U   T                     D   D   I   F     F     E     '
      'R R   E     N   N   T\nB   B U   U   T                     D   D   I   F     F     E     R  R  E     N  NN'
      '   T\nBBBB   UUU    T                     DDDD  IIIII F     F     EEEEE R   R EEEEE N   N   T')

end = timer()
print(end - start)
