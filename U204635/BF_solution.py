from itertools import permutations

n = int(input())
distance = [
    [int(i) for i in input().split()]
    for _ in range(n)
]

ans = 0b1 << 32

for case in permutations(range(1, n), n-1):
    this = i = 0
    for j in case:
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
