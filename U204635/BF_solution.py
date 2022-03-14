from itertools import permutations


def solve(n, time_map):
    ans = 0b1 << 32

    for case in permutations(range(1, n), n - 1):
        this = i = 0
        for j in case:
            tmp = time_map[i][j]
            if tmp == -1:
                break
            this += tmp
            i = j
            if this >= ans:
                break
        else:
            ans = this

    return ans


if __name__ == '__main__':
    n = int(input())
    print(solve(n, [[int(i) for i in input().split()] for _ in range(n)]))
