size = 8


def neighbor(x, y):
    return [(x-1, y-2), (x+1, y-2), (x-1, y+2), (x+1, y+2), (x-2, y-1), (x+2, y-1), (x-2, y+1), (x+2, y+1)]

def valid(x, y):
    return 0 <= x < size and 0 <= y < size

def count(visited, x, y):
    return sum((xx, yy) not in visited and valid(xx, yy) for xx, yy in neighbor(x, y))

def find_bests(visited, x, y):
    return sorted(((count(visited, xx, yy), xx, yy) for xx, yy in neighbor(x, y) if (xx, yy) not in visited and valid(xx, yy)))

def travel(visited, x, y):
    if len(visited) == size * size:
        return [(x, y)]

    for _, xx, yy in find_bests(visited, x, y):
        if result := travel(visited | {(xx, yy)}, xx, yy):
            return [(x, y)] + result

if __name__ == '__main__':
    x, y = map(int, input().split())
    world = [[0] * size for _ in range(size)]
    for step, (i, j) in enumerate(travel({(x, y)}, x, y), start=1):
        world[i][j] = step

    print(*(' '.join(map(str, row)) for row in world), sep='\n')
