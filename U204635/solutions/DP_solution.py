def solve(n, time_map):
    past = {(0b1, 0): 0}  # (path, last) -> time
    for _ in range(n - 1):
        this = {}
        for key, spent in past.items():
            visited, last = key

            for i in range(1, n):
                if not visited & 0b1 << i:
                    time = time_map[last][i]
                    if time == -1:
                        continue

                    val = spent + time
                    key = visited | 0b1 << i, i
                    if key not in this or this[key] > val:
                        this[key] = val
        past = this

    return min(past.values())


if __name__ == '__main__':
    n = int(input())
    print(solve(n, [[int(i) for i in input().split()] for _ in range(n)]))
