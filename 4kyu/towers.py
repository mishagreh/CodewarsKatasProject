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
import math
from collections import deque
import pdb


class Turret:
    def __init__(self, letter, turret):
        self.name = letter
        self.range = turret[0]
        self.rate = turret[1]


class Path:
    def __init__(self, grid, turrets):
        self._ones = 0
        self.turrets_coord = {}
        self.path = self._build_path(grid)
        self.all_attacked_cells = self.t_range(turrets)

    def _build_path(self, grid):

        # Look for the start and turrets coordinates, counting '1's
        for i in grid:
            for j in i:
                if j == '0':
                    x = i.index(j)
                    y = grid.index(i)
                if j == '1':
                    self._ones += 1
                if j not in ('0', '1', ' '):
                    self.turrets_coord[f'{j}'] = (
                        i.index(j),
                        grid.index(i)
                    )

        # Scaning the area for '1's. 4 candidate cells around each '1'
        path = [(x, y)]
        for _ in range(self._ones):
            for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if (
                    (len(grid) > i >= 0) and
                    (len(grid) > j >= 0) and
                    (grid[j][i] == '1') and
                    (i, j) not in path
                ):
                    path.append((i, j))
                    x, y = i, j

        return path

    def t_range(self, turrets):

        all_attacked_cells = {}
        for turret in turrets:
            all_attacked_cells[turret] = []
            n = turrets[turret][0]
            x, y = self.turrets_coord[turret]
            for j in self.path:
                distance = math.dist((x, y), j)
                if 1 <= distance <= n:
                    all_attacked_cells[turret].append(j)

        return all_attacked_cells


def tower_defense(grid, turrets, aliens):
    path_and_attacked_cells = Path(grid, turrets)
    path = path_and_attacked_cells.path
    all_attacked_cells = path_and_attacked_cells.all_attacked_cells
    extra_path = [(-1, -1) for i in range(len(aliens))]
    path = path + extra_path
    move = deque(maxlen=len(aliens))

    for position in path:
        breakpoint()
        move.appendleft(position)

        targeted_cells = {}
        for i in all_attacked_cells:
            targeted = []
            for j in all_attacked_cells[i]:
                for k in move:
                    if (k == j) and (aliens[move.index(k)] != 0):
                        targeted.append(k)
            if targeted != []:
                targeted_cells[i] = targeted[::-1]

        all_turrets = {i: Turret(i, turrets[i]) for i in turrets}

        breakpoint()
        turrets_with_target = targeted_cells

        shots = sum((
            all_turrets[i].rate for i in turrets_with_target
        ))

        for shot in range(shots):
            turrets_with_target = tuple(filter(
                lambda x: all_turrets[x].rate > 0,
                turrets_with_target
            ))
            if turrets_with_target == ():
                break

            for turret in turrets_with_target:
                if targeted_cells[turret] == []:
                    continue

                for cell in targeted_cells[turret]:
                    ndx = move.index(targeted_cells[turret][0])

                    if aliens[ndx] == 0:
                        targeted_cells[turret] = list(filter(
                            lambda x: targeted_cells[turret].index(x) != 0,
                            targeted_cells[turret]
                        ))
                        if targeted_cells[turret] == []:
                            break
                        else:
                            continue
                    aliens[ndx] -= 1
                    all_turrets[turret].rate -= 1
                    break

    print(sum(aliens))
    return sum(aliens)


grid = [
 '1111111111',
 '1A      B1',
 '111C111111',
 '  1 1D    ',
 '011E111111',
 '        F1',
 'G1111111 1',
 '11  H  111',
 '1 I111  J ',
 '1111K11111'
]

# turrets = {'A': [1, 2], 'B': [1, 5], 'C': [1, 4], 'D': [3, 3], 'E': [4, 4],
#            'F': [1, 2], 'G': [2, 2], 'H': [1, 3], 'I': [3, 3], 'J': [1, 4],
#            'K': [1, 2]}
# aliens = [66, 44, 63, 0, 51, 44, 70, 0, 42, 70, 47, 63, 64, 58, 44, 69, 53,
# 0, 61, 63, 0, 42, 68, 0, 58, 65, 55, 51, 55, 56, 55, 58, 55, 52, 48]

turrets = {'A': [1, 2], 'B': [1, 5], 'C': [1, 3], 'D': [3, 2], 'E': [3, 3],
           'F': [1, 4], 'G': [3, 2], 'H': [1, 4], 'I': [2, 2], 'J': [1, 3],
           'K': [1, 2]}
aliens = [61, 54, 57, 58, 47, 50, 42, 49, 62, 56, 38, 57, 0, 0, 61, 56, 0,
          59, 43, 54, 58]

# The aliens that successfully breached our defenses:
# Alien [17] with [9] health
# : 10 should equal 9

if __name__ == '__main__':
    tower_defense(grid, turrets, aliens)
