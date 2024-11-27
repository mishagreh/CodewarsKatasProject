# https://www.codewars.com/kata/5a57faad880385f3b60000d0
#
# This kata is inspired by Tower Defense (TD), a subgenre of strategy
# video games where the goal is to defend a player's territories or
# possessions by obstructing enemy attackers, usually by placing defensive
# structures on or along their path of attack.
#
# Objective
# It's the future, and hostile aliens are attacking our planet. We've set up
# a defense system in the planet's outer perimeter. You're tasked with
# calculating the severity of a breach.
#
# Input
# Your function will receive three arguments:
#     Battle Area Map: An array/list of strings representing an n x n
#     battle area.
#     Each string will consist of any of the following characters:
#         0: entrance point (starting position on alien path)
#         1: alien path
#         " "(space character): not alien path
#         A - Z: turret positions
#     Turret Stats: An object/dict where keys are upper-case characters from
#     the English alphabet (A - Z) and the values are subarrays in the
#     following format:
#     [n,m] - where n is the attack range of a turret, and m is its shot
#     frequency per move
#     Alien Wave Stats: An array of integers representing each individual alien
#     in sequence. Each value is an integer representing the health points of
#     each alien; health points are the number of turret shots required to take
#     down a given alien. Integer zero (0) counts as a gap in sequence.
#
# Output
# Return the integer sum of total health points of all aliens that successfully
# penetrate our defense.
from pprint import pprint

battlefield = [
   '011  1111',
   ' A1  1BC1',
   ' 11  1 11',
   ' 1D  1 1E',
   ' 111 1F11',
   '  G1 1  1',
   ' 111 1 11',
   ' 1H  1 1I',
   ' 11111 11'
]

turrets = {'A': [3, 2], 'B': [1, 4], 'C': [2, 2], 'D': [1, 3]}

wave = [30, 14, 27, 21, 13, 0, 15, 17, 0, 18, 26]


class BattleArea:
    def __init__(self, battlefield):
        self.battlefield = battlefield

        # Total health points of all aliens
        # that successfully penetrated the area
        self.survivors = 0

    def move(self):
        pass


class Turrets:
    def __init__(self, turrets):
        self.turrets = turrets

    def damage(self):
        pass


class Wave:
    def __init__(self, wave):
        self.wave = wave


class Track:
    def __init__(self, battlefield):
        self.track = self._build_track(battlefield)

    def _build_track(self, battlefield):
        # pass
        ones = 0
        for i in battlefield:
            for j in i:
                if j == '0':
                    x = i.index(j)
                    y = battlefield.index(i)
                elif j == '1':
                    ones += 1
                continue
        print(x, y)
        print(ones)

        self.track = [(x, y)]
        while ones > 0:
            try:
                if (x-1 >= 0) and (y >= 0) and battlefield[y][x-1] == '1' and (x-1, y) not in self.track:
                    self.track.append((x-1, y))
                    x, y = x-1, y
                    print(1, x, y)
            except Exception:
                print(Exception)
                # continue
            try:
                if (x+1 >= 0) and (y >= 0) and battlefield[y][x+1] == '1' and (x+1, y) not in self.track:
                    self.track.append((x+1, y))
                    x, y = x+1, y
                    print(2, x, y)
            except Exception:
                print(Exception)
                # continue
            try:
                if (x >= 0) and (y-1 >= 0) and battlefield[y-1][x] == '1' and (x, y-1) not in self.track:
                    self.track.append((x, y-1))
                    x, y = x, y-1
                    print(3, x, y)
            except Exception:
                print(Exception)
                # continue
            try:
                if (x >= 0) and (y+1 >= 0) and battlefield[y+1][x] == '1' and (x, y+1) not in self.track:
                    self.track.append((x, y+1))
                    x, y = x, y+1
                    print(4, x, y)
            except Exception:
                print(Exception)
                # continue

            finally:
                ones -= 1
                print(ones)
        print(self.track)
        pprint(battlefield)


class Turret:
    def __init__(self, track, turret):
        self.attacked_cells = self._define_attacked_cells(track, turret)

    def _define_attacked_cells(self, track, turret):
        pass


if __name__ == '__main__':
    # area = BattleArea(battlefield)
    # turrets = Turrets(turrets)
    # wave = Wave(wave)
    # while True:
    #     area.move()
    #
    track = Track(battlefield)
