def solve(n, a, b):
    # return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return [sum(a[i][k] * b[k][j] for k in range(n)) for i in range(n) for j in range(n)]


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    a = [numbers[i * n:i * n + n] for i in range(n)]
    b = [numbers[i * n:i * n + n] for i in range(n, n + n)]

    print(" ".join(map(str, solve(n, a, b))))
