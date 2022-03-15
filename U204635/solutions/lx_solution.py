__author__ = "@MTX5148635"


def solve(n, time_map):
    sumCost = pow(2, 31)

    def compare(numList):
        sum_ = 0
        nonlocal sumCost, time_map
        for i in range(len(numList) - 1):
            x = numList[i]
            y = numList[i + 1]
            if time_map[x][y] == -1:
                return -1
            sum_ += time_map[x][y]
        if sum_ < sumCost:
            sumCost = sum_

    def perm(numList, start, end):
        if start == end:
            compare(numList)
        else:
            for i in range(start, end):
                numList[start], numList[i] = numList[i], numList[start]
                perm(numList, start + 1, end)
                numList[start], numList[i] = numList[i], numList[start]

    nums = [i for i in range(n)]
    perm(nums, 1, n)

    return sumCost


if __name__ == '__main__':
    n = int(input())
    print(solve(n, [[int(i) for i in input().split()] for _ in range(n)]))
