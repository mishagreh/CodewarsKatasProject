# https://www.codewars.com/kata/5a57faad880385f3b60000d0
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
import math
from itertools import product, zip_longest, takewhile
from collections import deque


battlefield = [
    '0111111',
    '  A  B1',
    ' 111111',
    ' 1     ',
    ' 1C1111',
    ' 111 D1',
    '      1'
]

turrets = {'A': [3, 2], 'B': [1, 4], 'C': [2, 2], 'D': [1, 3]}
# turrets = {'D': [1, 3]}

wave = [30, 14, 27, 21, 13, 0, 15, 17, 0, 18, 26]
# wave = [4, 0, 9]


class BattleArea:
    def __init__(self, battlefield):
        self.battlefield = battlefield

        # Total health points of all aliens
        # that successfully penetrated the area
        self.survivors = 0

    def move(self):
        pass


class Turret:
    def __init__(self, name, turret):
        self.name = name
        self.range = turret[0]
        self.rate = turret[1]
        # self.all_attacked_cells = self.t_range()

    def damage(self):
        pass


class Wave:
    def __init__(self, wave):
        self.wave = wave


class Track:
    def __init__(self, battlefield):
        self._ones = 0
        self.turrets_coord = {}
        self.track = self._build_track(battlefield)
        self.all_attacked_cells = self.t_range()

    def _build_track(self, battlefield):

        # Looking for the start point coordinates and counting '1's
        for i in battlefield:
            for j in i:
                if j == '0':
                    x = i.index(j)
                    y = battlefield.index(i)
                elif j == '1':
                    self._ones += 1
                elif j not in ('0', '1', ' '):
                    self.turrets_coord[f'{j}'] = (
                        i.index(j),
                        battlefield.index(i)
                    )

        # Scaning the area for '1's. 4 candidate cells around each '1'
        track = [(x, y)]
        while self._ones > 0:
            for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                try:
                    if (
                        (i >= 0) and
                        (j >= 0) and
                        battlefield[j][i] == '1' and
                        (i, j) not in track
                    ):
                        track.append((i, j))
                        x, y = i, j
                except Exception:
                    pass
                    # print('Exception occured.')
                    # print('The candidate cell is beyond the area.')
                    # print('Or taken into account already.')
            self._ones -= 1
        # print(track)

        return track

    def t_range(self):

        all_attacked_cells = {}
        length = len(battlefield)
        for i in turrets:
            n = turrets[i][0]
            damage = turrets[i][1]
            x, y = self.turrets_coord[i]
            turret_attacked_cells = []

            x_coords = map(sum, product([x], range(-n, n+1)))
            y_coords = map(sum, product([y], range(-n, n+1)))
            all_coords = list(product(x_coords, y_coords))
            for j in all_coords:
                distance = math.dist((x, y), j)
                c1 = length >= j[0] >= 0
                c2 = length >= j[1] >= 0
                c3 = j != (x, y)
                c4 = distance <= n
                if c1 and c2 and c3 and c4:
                    turret_attacked_cells.append(j)
            # print(f'turret_attacked_cells: {turret_attacked_cells}')

            attacked = []
            # print(self.track)
            for _ in self.track:
                if _ in turret_attacked_cells:
                    attacked.append(_)
            # print(f'attacked: {attacked}')
            # all_attacked_cells.append(attacked)
            all_attacked_cells[i] = {
                'attacked_cells': attacked[::-1],
                'damage': damage
            }
            # all_attacked_cells[i]['damage'] = damage
        pprint(all_attacked_cells)
        return all_attacked_cells


def main(battlefield, turrets, wave):
    x = Track(battlefield)
    track = x.track
    all_turrets = x.all_attacked_cells
    print(wave)
    extra_track = [(-1, -1) for i in range(len(wave))]
    print(extra_track)
    # track = track.append(extra_track)
    track = track + extra_track
    print(track)
    # print(len(wave))
    z = deque(maxlen=len(wave))
    for i in track:
        z.appendleft(i)
        # print(z)
        qq = list(takewhile(lambda x: x[1] is not None, zip_longest(wave, z)))
        print(qq)

        # turrets = [print(turrets[i]) for i in turrets]
        the_turrets = [Turret(i, turrets[i]) for i in turrets]
        # turrets = [Turret(i) for i in turrets]

        for i, (health, cell) in enumerate(qq):
            # print(position[1])
            if health == 0:
                continue

            current_cell_attackers = list(filter(
                lambda x: cell in all_turrets[x.name]['attacked_cells'], the_turrets
            ))

            print(current_cell_attackers)
            if current_cell_attackers == []:
                continue
            else:
                shots = sum([i.rate for i in current_cell_attackers])
                print(shots)
                for shot in range(shots):
                    current_cell_attackers = list(filter(lambda i: i.rate != 0, current_cell_attackers))
                    print(current_cell_attackers)
                    for turret in current_cell_attackers:
                        if health == 0:
                            break
                        # print(turret)
                        health -= 1
                        turret.rate -= 1
                    wave[i] = health
    print(wave)
    # print(damage)


if __name__ == '__main__':
    main(battlefield, turrets, wave)
