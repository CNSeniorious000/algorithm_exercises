def solve(n, time_map):
    past = {(0b1, 0): 0}  # (path, last) -> time
    for _ in range(n - 1):
        this = {}
        for case, time in past.items():
            path, last = case

            for i in range(1, n):
                if not path & 0b1 << i:
                    tmp = time_map[last][i]
                    if tmp == -1:
                        continue

                    val = time + tmp
                    key = path | 0b1 << i, i
                    if key not in this or this[key] > val:
                        this[key] = val
        past = this

    return min(past.values())


if __name__ == '__main__':
    n = int(input())
    print(solve(n, [[int(i) for i in input().split()] for _ in range(n)]))
