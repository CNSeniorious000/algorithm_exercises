from contextlib import contextmanager
from matplotlib import pyplot as plt
from math import factorial
import numpy as np
import pickle

x, y_0, y_1, y_2, y_3 = pickle.load(open("out.pkl", "rb"))

ys = [y_0, y_1, y_2, y_3]
labels = """
depth-first searching solution
brute force solution (in pure python)
brute force solution (with built-in C functions)
dynamic programming solution
""".strip().split("\n")


which = range(4)
# which = [0, 2, 3]


@contextmanager
def new(filename):
    yield plt.figure(figsize=(15, 10), dpi=175)
    plt.savefig(f"plots/{filename}_{which}.svg")
    plt.savefig(f"plots/{filename}_{which}.png")
    plt.show()
    plt.close("all")


def show_raw_time():
    with new(1):
        for i in which:
            plt.plot(x, ys[i], label=labels[i])
        plt.xlabel(r"$n$")
        plt.ylabel(r"$t(n)$")
        plt.title("time complexity among different algorithms")
        plt.legend()


def show_ratio_tests_1():
    with new(2):
        for i in which:
            plt.plot(x, [ys[i][j] / factorial(k) for j, k in enumerate(x)], label=labels[i])
        plt.xlabel(r"$n$")
        plt.ylabel(r"\frac{t(n)}{n!}")
        plt.title("ratio tests among different algorithms")
        plt.legend()


def show_ratio_tests_2():
    with new(3):
        for i in which:
            plt.plot(x, [ys[i][j] / k for j, k in enumerate(x)], label=labels[i])
        plt.xlabel(r"$n$")
        plt.ylabel(r"\frac{t(n)}{n}")
        plt.title("ratio tests among different algorithms")
        plt.legend()


def show_power_tests():
    with new(4):
        for i in which:
            plt.plot(np.log(x), np.log(ys[i]), label=labels[i])
        plt.xlabel(r"$ln(n)$")
        plt.ylabel(r"$ln(t(n)$")
        plt.title("power tests among different algorithms")
        plt.legend()


if __name__ == '__main__':
    show_raw_time()
    show_ratio_tests_1()
    show_ratio_tests_2()
    show_power_tests()
