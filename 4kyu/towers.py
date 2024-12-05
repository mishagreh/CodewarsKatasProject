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
from collections import deque
from itertools import takewhile
from operator import sub


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

        pprint(self.turrets_coord)

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

        print(path)
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


# def tower_defense(grid, turrets, aliens):
#     x = Path(grid, turrets)
#     path = x.path
#     all_turrets = x.all_attacked_cells
#     pprint(all_turrets)
#     extra_path = [(-1, -1) for i in range(len(aliens))]
#     path = path + extra_path
#     z = deque(maxlen=len(aliens))
#     for q in path:
#         z.appendleft(q)
#         qq = list(zip(aliens, z))
#         print(qq)
#         print(' ')
#
#         the_turrets = [Turret(i, turrets[i]) for i in turrets]
#
#         for i, (health, cell) in enumerate(qq):
#             if health == 0:
#                 continue
#             else:
#                 current_cell_attackers = list(filter(
#                     lambda x: cell in all_turrets[x.name],
#                     the_turrets
#                 ))
#
#                 if i == 26:
#                     print('alien:', i)
#                     print('health in aliens:', aliens[i])
#                     print('health in path:', health)
#                     print('cell in path:', cell)
#                     for f in current_cell_attackers:
#                         print('attacker:', f.name, 'range:', f.range, 'rate:', f.rate)
#
#                 # print(current_cell_attackers)
#                 if current_cell_attackers == []:
#                     continue
#                 else:
#                     shots = sum([i.rate for i in current_cell_attackers])
#                     if shots == 0:
#                         continue
#                     if i == 26:
#                     # print('before shooting, alien number:', i)
#                         print('shots planned:', shots)
#                     # print(shots)
#                     for shot in range(shots):
#                         if health == 0:
#                             break
#                         else:
#                             current_cell_attackers = list(
#                                 filter(lambda i: i.rate > 0, current_cell_attackers)
#                             )
#                         # if i == 28:
#                         # print('shooting:', current_cell_attackers)
#                         # print(current_cell_attackers)
#
#                             for turret in current_cell_attackers:
#                         # #     print('before', 'i:', i, 'health:', health, 'cell:', cell)
#                         # #     print('range')
#                         # #     pprint(all_turrets[turret.name]['attacked_cells'])
#                         # #     print('path before shooting:', qq)
#                                 if health == 0:
#                                     shots1 = sum([i.rate for i in current_cell_attackers])
#                                     print(i, cell)
#                                     print('health became 0, shots left', shots1)
#                                     break
#                                 else:
#                                     health -= 1
#                                     turret.rate -= 1
#                                     qq[i] = health, cell
#                                     # print('path after shooting:', qq)
#                                     aliens[i] = health
#                                     # print('after', 'i:', i, 'health:', health, 'cell:', cell)
#     print(aliens)
#     print(sum(aliens))
#     return sum(aliens)


# grid = [
#     '0111111',
#     '  A  B1',
#     ' 111111',
#     ' 1     ',
#     ' 1C1111',
#     ' 111 D1',
#     '      1'
# ]
#
# turrets = {'A': [3, 2], 'B': [1, 4], 'C': [2, 2], 'D': [1, 3]}
# aliens = [30, 14, 27, 21, 13, 0, 15, 17, 0, 18, 26]

def tower_defense(grid, turrets, aliens):
    x = Path(grid, turrets)
    path = x.path
    all_turrets = x.all_attacked_cells
    # pprint(all_turrets)
    extra_path = [(-1, -1) for i in range(len(aliens))]
    path = path + extra_path
    z = deque(maxlen=len(aliens))
    # for q in path[:5]:
    for q in path:
        z.appendleft(q)
        # print('______')
        # print(' ')

        new_dict = {}
        for i in all_turrets:
            targeted = []
            for j in all_turrets[i]:
                for k in z:
                    if k == j:
                        targeted.append(k)
            new_dict[i] = targeted[::-1]

        # pprint(new_dict)

        the_turrets = {i: Turret(i, turrets[i]) for i in turrets}

        # for turret in new_dict:
        turrets_with_target = tuple(filter(lambda x: new_dict[x] != [], new_dict))
        print(turrets_with_target)
        shots = sum((
            the_turrets[i].rate for i in turrets_with_target
        ))
        # print('new_dict shots', shots)
        for shot in range(shots):
            turrets_with_target = tuple(filter(lambda x: the_turrets[x].rate > 0, turrets_with_target))
            print(turrets_with_target)
            for turret in turrets_with_target:
                print('___')
                print(aliens)
                print(turret)
                if new_dict[turret] == []:
                    continue
                ndx = z.index(new_dict[turret][0])
                print(ndx)
                print(new_dict[turret][0])
                print(aliens[ndx])
                if aliens[ndx] == 0:
                    new_dict[turret].pop(0)
                    break
                aliens[ndx] -= 1
                the_turrets[turret].rate -= 1
                print(aliens)

    print(aliens)
    print(sum(aliens))


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
# aliens = [66, 44, 63, 0, 51, 44, 70, 0, 42, 70, 47, 63, 64, 58, 44, 69, 53, 0,
#           61, 63, 0, 42, 68, 0, 58, 65, 55, 51, 55, 56, 55, 58, 55, 52, 48]

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
