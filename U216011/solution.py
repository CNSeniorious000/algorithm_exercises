def solve(n, matrix, v):
    ans = matrix[v].copy()
    to_scan = set(range(n)) - {v}
    for _ in range(n - 1):
        to_scan.remove(
            index := min((i for i in to_scan if ~ans[i]), key=lambda x: ans[x])
        )
        total = ans[index]
        row = matrix[index]
        for i in to_scan:
            if ~row[i] and ((dist := row[i] + total) < ans[i] or ans[i] == -1):
                ans[i] = dist

    return ans[:v] + ans[v + 1:]


if __name__ == '__main__':
    print(*map(str, solve(lth := next(numbers := map(int, input().split())),
                          [[next(numbers) for _ in range(lth)] for _ in range(lth)],
                          next(numbers))), end="")
