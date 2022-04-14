def count(n):
    if n < 2:
        return n

    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, (a + b) % 100007

    return b


if __name__ == '__main__':
    print(count(int(input()) - 1))
