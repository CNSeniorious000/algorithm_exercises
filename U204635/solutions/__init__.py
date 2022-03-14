from alive_progress import alive_it as track
from itertools import combinations
import random

_MAX = 0b1 << 31


def generate_testcase(n, ratio=1):
    MAX = _MAX // n
    world = [[-1] * n for _ in range(n)]

    for i in range(n):
        world[i][i] = 0

    for i, j in track(combinations(range(n), 2), title="seeding", total=n * (n - 1) // 2):
        world[i][j] = world[j][i] = random.randrange(MAX)

    for _ in track(range(int(n * n * (1 - ratio))), title="dropping"):
        while True:
            i, j = random.randrange(n), random.randrange(n)
            if i != j and sum(world[i]) > 3 - n and sum(world[j]) > 3 - n:
                world[i][j] = world[j][i] = -1
                break

    return world


example_testcase = (5, [
    [0, 3, 6, -1, 1],
    [3, 0, 2, -1, 4],
    [6, 2, 0, 2, 3],
    [-1, -1, 2, 0, 1],
    [1, 4, 3, 1, 0]
])

if __name__ == '__main__':
    from wyh_solution import solve
    assert solve(*example_testcase) == 6

    from BF_solution import solve
    assert solve(*example_testcase) == 6

    from DP_solution import solve
    assert solve(*example_testcase) == 6
