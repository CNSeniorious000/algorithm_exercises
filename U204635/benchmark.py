from solutions.wyh_solution import solve as solve_0
from solutions.BF_solution import solve as solve_1
from solutions.DP_solution import solve as solve_2
from time import perf_counter as time
from solutions import generate_testcase
from contextlib import contextmanager
from contextlib import suppress
from rich import print


@contextmanager
def timer(func):
    t = time()
    yield
    print(func.__name__, time() - t)


def run(func, *args, n=10_000):
    with timer(func):
        t = time()
        for _ in range(n):
            func(*args)
        return time() - t


def do_test(size, ratio, m=100, n=100):
    cases = [
        generate_testcase(size, ratio)
        for _ in range(m)
    ]

    return [
        sum(run(func, size, case, n=n) for case in cases)/(m*n)
        for func in (solve_0, solve_1, solve_2)
    ]


def plot():
    from matplotlib import pyplot as plt
    ratio = 0.9
    x, y_0, y_1, y_2 = [], [], [], []
    with suppress(KeyboardInterrupt):
        for size in range(4, 12):
            print(f"{size = }, {ratio = }")
            x.append(size)
            a, b, c = do_test(size, ratio)
            y_0.append(a)
            y_1.append(b)
            y_2.append(c)

    limit = min(len(x), len(y_0), len(y_1), len(y_2))

    plt.plot(x[:limit], y_0[:limit])
    plt.plot(x[:limit], y_1[:limit])
    plt.plot(x[:limit], y_2[:limit])
    plt.show()


if __name__ == '__main__':
    plot()
