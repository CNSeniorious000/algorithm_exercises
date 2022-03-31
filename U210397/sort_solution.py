def solve(n, k, lst):
    lst.sort()
    return lst[k]


if __name__ == '__main__':
    it = iter(map(int, input().split()))
    print(solve(next(it), next(it) - 1, list(it)))
