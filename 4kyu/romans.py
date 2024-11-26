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

        di = {
            '3': {'x': 'M', 'y': 'undefined', 'z': 'undefined'},
            '2': {'x': 'C', 'y': 'D', 'z': 'M'},
            '1': {'x': 'X', 'y': 'L', 'z': 'C'},
            '0': {'x': 'I', 'y': 'V', 'z': 'X'}
        }
        res = ''
        str_val = str(input)

        for i in range(len(str_val)):
            if int(str_val[i]):
                x = di[str(len(str_val)-1-i)]['x']
                y = di[str(len(str_val)-1-i)]['y']
                z = di[str(len(str_val)-1-i)]['z']

                digits = {
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
                res += digits[str_val[i]]
            else:
                continue

        return res

    @staticmethod
    def from_roman(input: str) -> int:

        di = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        sum = 0
        buf = ' '
        for i in input:
            if (i in 'VX') and (buf == 'I') or \
                (i in 'LC') and (buf == 'X') or \
                    (i in 'DM') and (buf == 'C'):
                sum += -2*di[buf] + di[i]
            else:
                sum += di[i]
            buf = i

        return sum


if __name__ == '__main__':
    print(RomanNumerals('LXXXVI').res)
