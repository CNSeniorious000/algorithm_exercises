class Solution:
    def __init__(self, n, w_max, w, v):
        self.i_max = n - 1
        self.w_max = w_max
        self.w = w
        self.v = v
        self.answers = [][]

    @cache
    def maximize(self, i, w_max):
        w, v = self.w, self.v
        if i == 0:
            return v[0] if w_max >= w[0] else 0
        else:
            return max(
                self.answers[i - 1][w_max],
                self.answers[i - 1][w_max - w[i]] + v[i]
            ) if w_max >= w[i] else self.maximize(i + 1, w_max)

    def solve(self):
        return self.maximize(0, self.w_max)


if __name__ == '__main__':
    values = map(int, input().split())
    n = next(values)
    print(Solution(n, next(values),
                   [next(values) for _ in range(n)],
                   [next(values) for _ in range(n)]).solve())
