def solve(lst: list, num: int) -> int:
    if lst[0] < num < lst[-1]:
        lth = len(lst)
        l, r = 0, lth - 1
        while l < r:
            index = (l + r) // 2
            value = lst[index]
            if value < num:
                l = index
            elif value > num:
                r = index
            else:
                return index
    return -1


if __name__ == '__main__':
    from contextlib import suppress

    with suppress(EOFError):
        while True:
            s = input().split()
            print(solve(list(map(int, s[1:-1])), int(s[-1])))
