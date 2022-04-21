def cache(func):
    memo = {}

    def inner(i, j):
        ans = memo.get((i, j), None)
        if ans is None:
            ans = memo[i, j] = func(i, j)
        return ans

    return inner


@cache
def levenshtein(i, j):
    if min(i, j) == -1:
        return max(i, j) + 1
    else:
        return min(
            levenshtein(i - 1, j) + 1,
            levenshtein(i, j - 1) + 1,
            levenshtein(i - 1, j - 1) + int(s1[i] != s2[j])
        )


if __name__ == '__main__':
    from sys import setrecursionlimit

    setrecursionlimit(12345678)
    s1, s2 = input().split()

    print(levenshtein(len(s1) - 1, len(s2) - 1))
