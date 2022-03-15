from alive_progress import alive_it as track
from itertools import combinations, permutations
import random

_MAX = 0b1 << 31


def generate_testcase(n, ratio=1):
    MAX = _MAX // n
    time_map = [[-1] * n for _ in range(n)]

    track = lambda *args, **kwargs: args[0]

    while True:
        for i in range(n):
            time_map[i][i] = 0

        for i, j in track(combinations(range(n), 2), title="seeding", total=n * (n - 1) // 2):
            time_map[i][j] = time_map[j][i] = random.randrange(MAX)

        for _ in track(range(int(n * n * (1 - ratio))), title="dropping"):
            while True:
                i, j = random.randrange(n), random.randrange(n)
                if i != j and time_map[i][j] != -1:
                    time_map[i][j] = -1
                    break
        
        if check_connect(time_map):
            return time_map


def check_connect(time_map):
    n = len(time_map)
    for path in permutations(range(1, n), n - 1):
        i = 0
        for j in path:
            if ~ time_map[i][j]:
                i = j
            else:
                break
        else:
            # print(path)
            return True
    return False


if __name__ == '__main__':
    example_testcase = (5, [
        [0, 3, 6, -1, 1],
        [3, 0, 2, -1, 4],
        [6, 2, 0, 2, 3],
        [-1, -1, 2, 0, 1],
        [1, 4, 3, 1, 0]
    ])

    from wyh_solution import solve
    assert solve(*example_testcase) == 6

    from lx_solution import solve
    assert solve(*example_testcase) == 6

    from BF_solution import solve
    assert solve(*example_testcase) == 6

    from DP_solution import solve
    assert solve(*example_testcase) == 6
