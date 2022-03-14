import random


def generate_testcase(n):
    raise NotImplementedError


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
