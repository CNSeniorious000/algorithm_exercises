while True:
    try:
        s = input().split()
    except EOFError:
        break

    lst = list(map(int, s[1:-1]))
    num = int(s[-1])

    try:
        print(lst.index(num))
    except ValueError:
        print(-1)