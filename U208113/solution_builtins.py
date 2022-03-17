def solve(lst: list, num: int) -> int:
    try:
        return lst.index(num)
    except ValueError:
        return -1


if __name__ == '__main__':
    from contextlib import suppress

    with suppress(EOFError):
        while True:
            s = input().split()
            print(solve(list(map(int, s[1:-1])), int(s[-1])))
