# Write two functions that convert a roman numeral to and from an
# integer value. Multiple roman numeral values will be tested for
# each function.
#
# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
# 2008, 'MMVIII', 1666 -> "MDCLXVI"

# 1000 - M
# 600 - DC
# 60 - LX
# 6 -> VI"

# {'I': 1, 'II': 2, 'III': 3, 'IV': 4,
# 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
# 'X': 10}

# I V X C D M


class RomanNumerals:

    def __init__(self, input):
        self.res = self.from_roman(input) if type(input) is str \
            else self.to_roman(input)

    @staticmethod
    def to_roman(input: int) -> str:

        pos = 'IVX', 'XLC', 'CDM', 'M  '
        res = ''
        str_input = str(input)

        for i, j in enumerate(str_input):

            x, y, z = (pos[len(str_input)-1-i][n] for n in (0, 1, 2))

            digits = {
                '0': '',
                '1': f'{x}',
                '2': 2*f'{x}',
                '3': 3*f'{x}',
                '4': f'{x}{y}',
                '5': f'{y}',
                '6': f'{y}{x}',
                '7': f'{y}' + 2*f'{x}',
                '8': f'{y}' + 3*f'{x}',
                '9': f'{x}{z}'
            }
            res += digits[j]

        return res

    @staticmethod
    def from_roman(input: str) -> int:

        letters = {
            'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
        }

        sum = 0
        buf = ' '
        for i in input:
            cond_1 = (i in 'VX') and (buf == 'I')
            cond_2 = (i in 'LC') and (buf == 'X')
            cond_3 = (i in 'DM') and (buf == 'C')
            if cond_1 or cond_2 or cond_3:
                sum += letters[i] - 2*letters[buf]
            else:
                sum += letters[i]
            buf = i

        return sum


if __name__ == '__main__':
    print(RomanNumerals(2000).res)
