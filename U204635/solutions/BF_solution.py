from itertools import permutations


def solve(n, time_map):
    ans = 0b1 << 31

    for path in permutations(range(1, n), n - 1):
        this = i = 0
        for j in path:
            time = time_map[i][j]
            if time == -1:
                break
            this += time
            i = j
            if this >= ans:
                break
        else:
            ans = this

    return ans


if __name__ == '__main__':
    n = int(input())
    print(solve(n, [[int(i) for i in input().split()] for _ in range(n)]))
