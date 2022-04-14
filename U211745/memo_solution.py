from functools import cache


class Solution:
    def __init__(self, i_max, w_max, w, v):
        self.i_max = i_max
        self.w_max = w_max
        self.w = w
        self.v = v

    @cache
    def maximize(self, i, w_max):
        w, v = self.w, self.v
        if i == self.i_max:
            return v[i] if w_max >= w[i] else 0
        else:
            return max(
                self.maximize(i + 1, w_max),
                self.maximize(i + 1, w_max - w[i]) + v[i]
            ) if w_max >= w[i] else self.maximize(i + 1, w_max)

    @property
    def answer(self):
        return self.maximize(0, self.w_max)


if __name__ == '__main__':
    values = map(int, input().split())
    n = next(values)
    print(Solution(n - 1, next(values),
                   [next(values) for _ in range(n)],
                   [next(values) for _ in range(n)]).answer)
