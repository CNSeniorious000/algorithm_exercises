"""solution from @w1742910621"""


def solve(n, time_map):
    best_path = [0]
    minimum_cost = pow(2, 31)

    def dfs(path, order, cost):
        nonlocal minimum_cost
        path.append(order)

        if len(path) == n:
            if cost < minimum_cost:
                best_path[-1] = path
                minimum_cost = cost
            return

        for i in range(n):
            if time_map[order][i] != -1 and i not in path and cost + time_map[order][i] < minimum_cost:
                cost += time_map[order][i]
                dfs(path.copy(), i, cost)
                cost -= time_map[order][i]

    dfs([], 0, 0)
    
    return minimum_cost


if __name__ == '__main__':
    n = int(input())
    print(solve(n, [[int(i) for i in input().split()] for _ in range(n)]))
