from itertools import permutations

n = int(input())
all_ = list(range(n))

distance = [
    [int(i) for i in input().split()]
    for _ in all_
]

ans = 1 << 32

for case in permutations(all_, n):
    this = 0
    it = iter(case)
    i = next(it)
    if i != 0:
        continue
    for j in it:
        tmp = distance[i][j]
        if tmp == -1:
            break
        this += tmp
        i = j
        if this >= ans:
            break
    else:
        ans = this

print(ans)
