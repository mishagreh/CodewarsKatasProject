# https://www.codewars.com/kata/5324945e2ece5e1f32000370
#
# Given the string representations of two integers, return the string
# representation of the sum of those integers.
#
# For example:
#
# sumStrings('1','2') // => '3'
#
# A string representation of an integer will contain no characters besides
# the ten numerals "0" to "9".
# Python: your solution need to work with huge numbers (about a milion digits),
# converting to int will not work.
#
# Top 1 solution is as follows:
#
# def sum_strings(x, y):
#     l, res, carry = max(len(x), len(y)), "", 0
#     x, y = x.zfill(l), y.zfill(l)
#     for i in range(l-1, -1, -1):
#         carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
#         res += str(d)
#     return ("1" * carry + res[::-1]).lstrip("0") or "0"


class Sum:

    def __init__(self, x, y):
        self._overflow = '0'
        self.result = self._calculate(x, y)

    def _action(self, x, y):
        """ The addition of two inputs itself via ints. """

        sum = int(x) + int(y) + int(self._overflow)

        if sum >= 10:
            next_digit = str(sum)[1]
            self._overflow = '1'
        else:
            next_digit = str(sum)
            self._overflow = '0'

        return next_digit

    def _calculate(self, x, y):
        """ Iterates over the input sequences and returns the final result. """

        len_x = len(x)
        len_y = len(y)
        if len_x == len_y:
            pass
        else:
            if len_x > len_y:
                y = y.zfill(len_x)
            else:
                x = x.zfill(len_y)
        x = x[::-1]
        y = y[::-1]

        output = list(
            map(self._action, x, y)
        )
        if int(self._overflow):
            output.append(self._overflow)
        result = ''.join(output[::-1]).lstrip('0')
        if result == '':
            return '0'
        else:
            return result


def sum_strings(x, y):
    """ Initial verification and passing the inputs into calculation. """

    if x and not y:
        return x
    elif y and not x:
        return y
    else:
        return Sum(x, y).result


if __name__ == '__main__':
    print(sum_strings('0', '0'))
