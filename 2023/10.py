import networkx

from utils.input import aoc

ip = aoc(2023, 10)
lines = [line for line in ip.splitlines()]
width = len(lines[0])
height = len(lines)

C = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(1, 0), (0, 1)],
    'S': [],
}

# Find the edges from the starting position 'S'
[(sx, sy)] = [(x, y) for y in range(height) for x in range(width) if lines[y][x] == 'S']
for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    i, j = sx + dx, sy + dy
    if lines[j][i] == '.':
        continue
    for di, dj in C[lines[j][i]]:
        if sx == i + di and sy == j + dj:
            C['S'].append((dx, dy))

# Construct a directed graph of the pipes
G = networkx.DiGraph()
for y, xs in enumerate(lines):
    for x, c in enumerate(xs):
        if c == '.':
            continue
        G.add_node((x, y))
        for dx, dy in C[c]:
            G.add_edge((x, y), (x + dx, y + dy))


def part1():
    return max(map(len, networkx.simple_cycles(G))) // 2


# Adapted from https://stackoverflow.com/a/63436180
def is_interior(point, polygon):
    def between(p, a, b):
        return a <= p <= b or a >= p >= b

    i, j = point
    inside = False
    for (x1, y1), (x2, y2) in zip(polygon, polygon[1:] + polygon[:1]):
        if point == (x1, y1) or point == (x2, y2):
            return False
        if y1 == y2 and j == y1 and between(i, x1, x2):
            return False
        if between(j, y1, y2):
            if j == y1 and y2 >= y1 or j == y2 and y1 >= y2:
                continue
            c = (x1 - i) * (y2 - j) - (x2 - i) * (y1 - j)
            if c == 0:
                return False
            if (y1 < y2) == (c > 0):
                inside = not inside
    return inside


def part2():
    polygon = list(max(networkx.simple_cycles(G), key=lambda x: len(x)))
    return sum(is_interior((x, y), polygon) for y in range(height) for x in range(width))


print(part1())
print(part2())
