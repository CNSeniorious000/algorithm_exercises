from heapq import nsmallest


def solve(n, k, lst):
    return nsmallest(k, lst)[-1]


if __name__ == '__main__':
    it = iter(map(int, input().split()))
    print(solve(next(it), next(it), list(it)))
