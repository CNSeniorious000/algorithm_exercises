from copy import deepcopy
from functools import cache

x, y = map(int, input().split())


full = [()]


def valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def count(world, x, y):
    return sum(
        valid(x-1, y-2) and (x-1, y-1) not in world,
        valid(x+1, y-2) and world[x+1][y-2],
        valid(x-1, y+2) and world[x-1][y+2],
        valid(x+1, y+2) and world[x+1][y+2],
        valid(x-2, y-1) and world[x-2][y-1],
        valid(x+2, y-1) and world[x+2][y-1],
        valid(x-2, y+1) and world[x-2][y+1],
        valid(x+2, y+1) and world[x+2][y+1],
    )


def find_bests(world, x, y):
    ans = []
    if valid(x-1, y-2):
        ans.append((count(world, x-1, y-2), x-1, y-2))
    if valid(x+1, y-2):
        ans.append((count(world, x+1, y-2), x+1, y-2))
    if valid(x-1, y+2):
        ans.append((count(world, x-1, y+2), x-1, y+2))
    if valid(x+1, y+2):
        ans.append((count(world, x+1, y+2), x+1, y+2))
    if valid(x-2, y-1):
        ans.append((count(world, x-2, y-1), x-2, y-1))
    if valid(x+2, y-1):
        ans.append((count(world, x+2, y-1), x+2, y-1))
    if valid(x-2, y+1):
        ans.append((count(world, x-2, y+1), x-2, y+1))
    if valid(x+2, y+1):
        ans.append((count(world, x+2, y+1), x+2, y+1))
    return sorted(ans, reverse=True)


def travel(world, now):
    pass
