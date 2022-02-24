"""solution using dynamic program """


n = int(input())
time_map = [[int(i) for i in input().split()] for _ in range(n)]


def contains(path, i):
    return path & 0b1 << i


past = {(0b0, 1): 0}  # (path, last) -> time
for _ in range(n-1):
    this = {}
    for case, time in past.items():
        path, last = case
        for i in range(n):
            if not contains(path, i):
                tmp = time_map[last][i]
                if tmp == -1:
                    break
                val = time + tmp
                key = path | 0b1 << i, i
                if key not in this or this[key] > val:
                    this[key] = val
    past = this

print(min(past.values()))
