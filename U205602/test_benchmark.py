import solution


def solve_zyh(size, start):
    solution.size = size
    return solution.travel({start}, *start)


test_00 = lambda benchmark: benchmark(solve_zyh, 8, (0,0))
test_01 = lambda benchmark: benchmark(solve_zyh, 8, (0,1))
test_02 = lambda benchmark: benchmark(solve_zyh, 8, (0,2))
test_03 = lambda benchmark: benchmark(solve_zyh, 8, (0,3))
test_11 = lambda benchmark: benchmark(solve_zyh, 8, (1,1))
test_12 = lambda benchmark: benchmark(solve_zyh, 8, (1,2))
test_13 = lambda benchmark: benchmark(solve_zyh, 8, (1,3))
test_22 = lambda benchmark: benchmark(solve_zyh, 8, (2,2))
test_23 = lambda benchmark: benchmark(solve_zyh, 8, (2,3))
test_33 = lambda benchmark: benchmark(solve_zyh, 8, (3,3))
