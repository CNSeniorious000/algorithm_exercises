import bisect


def solve(lst, num):
    if num in lst:
        return bisect.bisect_left(lst, num)
    else:
        return -1


if __name__ == '__main__':
    while True:
        try:
            s = input().split()
        except EOFError:
            break
        print(solve(list(map(int, s[1:-1])), int(s[-1])))
