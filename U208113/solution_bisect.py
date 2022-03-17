import bisect


def solve(lst: list, num: int) -> int:
    if num in lst:
        return bisect.bisect_left(lst, num)
    else:
        return -1


if __name__ == '__main__':
    from contextlib import suppress

    with suppress(EOFError):
        while True:
            s = input().split()
            print(solve(list(map(int, s[1:-1])), int(s[-1])))
