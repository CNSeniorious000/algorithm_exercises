from solutions.wyh_solution import solve as solve_0
from solutions.lx_solution import solve as solve_1
from solutions.BF_solution import solve as solve_2
from solutions.DP_solution import solve as solve_3
from time import perf_counter as time
from solutions import generate_testcase
from contextlib import contextmanager
from contextlib import suppress
from rich import print


@contextmanager
def timer(func):
    t = time()
    yield
    print(func.__module__, time() - t)


def run_1(func, *args, n=10_000):
    with timer(func):
        t = time()
        for _ in range(n):
            func(*args)
        return time() - t

def run_2(func, *args, t=30):
    raise NotImplementedError(func, args, t)

def do_test_1(size, ratio, m=100, n=100):
    cases = [
        generate_testcase(size, ratio)
        for _ in range(m)
    ]

    return [
        sum(run_1(func, size, case, n=n) for case in cases) / (m * n)
        for func in (solve_0, solve_1, solve_2, solve_3)
    ]

def do_test_2(size, ratio, m=32, n=8):
    cases = [
        generate_testcase(size, ratio)
        for _ in range(m)
    ]

    return [
        sum(run_1(func, size, case, n=n) for case in cases) / (m * n)
        for func in (solve_0, solve_3)
    ]

def plot_1():
    from matplotlib import pyplot as plt
    ratio = 0.9
    x, y_0, y_1, y_2, y_3 = [], [], [], [], []
    with suppress(KeyboardInterrupt):
        for size in range(3, 9):
            print(f"{size = }, {ratio = }")
            x.append(size)
            a, b, c, d = do_test_1(size, ratio)
            y_0.append(a)
            y_1.append(b)
            y_2.append(c)
            y_3.append(d)

    limit = min(len(x), len(y_0), len(y_1), len(y_2))

    plt.plot(x[:limit], y_0[:limit], label="WYH")
    plt.plot(x[:limit], y_1[:limit], label="LX")
    plt.plot(x[:limit], y_2[:limit], label="ZYH-BF")
    plt.plot(x[:limit], y_3[:limit], label="ZYH-DP")
    plt.title("time complexity among different algorithms")
    plt.xlabel("n")
    plt.ylabel("time(s)")
    plt.legend()
    plt.show()

def plot_2():
    from matplotlib import pyplot as plt
    ratio = 1
    # x, y_0, y_3 = [], [], []
    x, y = [], []
    with suppress(KeyboardInterrupt):
        for size in range(3, 16):
            print(f"{size = }, {ratio = }")
            x.append(size)
            a, d = do_test_2(size, ratio)
            # y_0.append(a)
            # y_3.append(d)
            y.append(a / d)

    # limit = min(len(x), len(y_0), len(y_3))
    limit = min(len(x), len(y))

    # plt.plot(x[:limit], y_0[:limit], label="WYH")
    # plt.plot(x[:limit], y_3[:limit], label="ZYH-DP")
    plt.plot(x[:limit], y[:limit])
    plt.title("time complexity among different algorithms")
    plt.xlabel("n")
    # plt.ylabel("time(s)")
    plt.ylabel(r"$\frac{WYH}{ZYH\_DP}$")
    # plt.legend()
    plt.show()


if __name__ == '__main__':
    plot_2()
