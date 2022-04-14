def solve(n, k, lst):
    k -= 1
    l, r = 0, n - 1
    while True:
        i, j = l, r
        tmp = lst[j]
        while i < j:
            while i < j:
                if lst[i] <= tmp:
                    i += 1
                else:
                    lst[j] = lst[i]
                    j -= 1
                    break
            while i < j:
                if lst[j] >= tmp:
                    j -= 1
                else:
                    lst[i] = lst[j]
                    i += 1
                    break
        if j == k:
            return tmp
        else:
            lst[j] = tmp
        if j < k:
            l = j + 1
        else:
            r = j - 1


if __name__ == '__main__':
    it = iter(map(int, input().split()))
    print(solve(next(it), next(it), list(it)))
