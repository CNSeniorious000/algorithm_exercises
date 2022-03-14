from solutions.wyh_solution import solve as solve_0
from solutions.BF_solution import solve as solve_1
from solutions.DP_solution import solve as solve_2
from solutions import generate_testcase
from copy import deepcopy
from rich import *

def main():
    n, ratio = 10, 0.5
    case = generate_testcase(n, ratio)
    print(case)
    print(solve_0(n, deepcopy(case)))
    print(solve_1(n, deepcopy(case)))
    print(solve_2(n, deepcopy(case)))
    ans = [solve_0(n, deepcopy(case)), solve_1(n, deepcopy(case)), solve_2(n, deepcopy(case))]
    assert ans[0] == ans[1] == ans[2], case


if __name__ == '__main__':
    main()
