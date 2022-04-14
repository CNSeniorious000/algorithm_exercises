from sort_solution import solve as sort_solve
from heap_solution import solve as heap_solve
from quick_search_solution import solve as quick_solve
from random import randrange

n = 12345
k = 1234
lst = [randrange(1 << 32) for _ in range(n)]


def test_sort_solve(benchmark):
    benchmark(lambda n, k, lst: sort_solve(n, k, lst.copy()), n, k, lst)


def test_heap_solve(benchmark):
    benchmark(lambda n, k, lst: heap_solve(n, k, lst.copy()), n, k, lst)


def test_quick_solve(benchmark):
    benchmark(lambda n, k, lst: quick_solve(n, k, lst.copy()), n, k, lst)
