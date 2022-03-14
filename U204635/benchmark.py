from re import I
from solutions.wyh_solution import solve as solve_0
from solutions.BF_solution import solve as solve_1
from solutions.DP_solution import solve as solve_2
from time import perf_counter_ns as time
from solutions import generate_testcase
from contextlib import contextmanager
from copy import deepcopy
from numpy import array
from numba import jit
from rich import *


@contextmanager
def timer(func):
    t = time()
    yield
    print(func.__name__, time() - t)


solve_2 = jit(nopython=False, cache=True)(solve_2)

def main():
    n, ratio = 15, 0.98
    case = generate_testcase(n, ratio)

    with timer(solve_2):
        ans_2 = solve_2(n, array(case))
    
    with timer(solve_0):
        ans_0 = solve_0(n, deepcopy(case))

    with timer(solve_1):
        ans_1 = solve_1(n, deepcopy(case))

    assert ans_0 == ans_1 == ans_2, case


if __name__ == '__main__':
    main()
