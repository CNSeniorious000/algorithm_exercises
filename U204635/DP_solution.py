"""solution using dynamic program """

n = int(input())
time_map = [[int(i) for i in input().split()] for _ in range(n)]

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

print(min(past.values()))
