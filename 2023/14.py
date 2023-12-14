from functools import cache

from utils.input import aoc

ip = aoc(2023, 14)
G = [list(line) for line in ip.splitlines()]
STOP = 10000  # increase this if the answer is wrong, 10k is enough for my input
width, height = len(G[0]), len(G)

N = dict()
S = dict()
E = dict()
W = dict()
for y, row in enumerate(G):
    for x, c in enumerate(row):
        if c == '#':
            continue
        for j in range(y, -1, -1):
            if G[j][x] == '#':
                N[(x, y)] = j
                break
        else:
            N[(x, y)] = -1
        for j in range(y, height):
            if G[j][x] == '#':
                S[(x, y)] = j
                break
        else:
            S[(x, y)] = len(G)
        for i in range(x, width):
            if G[y][i] == '#':
                E[(x, y)] = i
                break
        else:
            E[(x, y)] = len(row)
        for i in range(x, -1, -1):
            if G[y][i] == '#':
                W[(x, y)] = i
                break
        else:
            W[(x, y)] = -1


def north(xs):
    ys = list(xs)
    cx, cy = 0, -1
    for i, (x, y) in enumerate(sorted(xs)):
        if x != cx:
            cy = -1
        cx = x
        cy = max(cy + 1, N[(x, y)] + 1)
        ys[i] = (x, cy)
    return tuple(ys)


def south(xs):
    ys = list(xs)
    cx, cy = 0, height
    for i, (x, y) in enumerate(sorted(xs, key=lambda x: (x[0], -x[1]))):
        if x != cx:
            cy = height
        cx = x
        cy = min(cy - 1, S[(x, y)] - 1)
        ys[i] = (x, cy)
    return tuple(ys)


def east(xs):
    ys = list(xs)
    cx, cy = width, 0
    for i, (x, y) in enumerate(sorted(xs, key=lambda x: (x[1], -x[0]))):
        if y != cy:
            cx = width
        cy = y
        cx = min(cx - 1, E[(x, y)] - 1)
        ys[i] = (cx, y)
    return tuple(ys)


def west(xs):
    ys = list(xs)
    cx, cy = -1, 0
    for i, (x, y) in enumerate(sorted(xs, key=lambda x: (x[1], x[0]))):
        if y != cy:
            cx = -1
        cy = y
        cx = max(cx + 1, W[(x, y)] + 1)
        ys[i] = (cx, y)
    return tuple(ys)


@cache
def cycle(xs):
    n = north(xs)
    w = west(n)
    s = south(w)
    e = east(s)
    return e


def part1():
    xs = list()
    for x in range(width):
        for y in range(height):
            if G[y][x] == 'O':
                xs.append((x, y))

    xs = north(xs)
    ans = 0
    for x, y in xs:
        ans += height - y
    return ans


def part2():
    xs = list()
    for x in range(width):
        for y in range(height):
            if G[y][x] == 'O':
                xs.append((x, y))

    xs = tuple(xs)
    A = dict()
    for i in range(STOP * 2):
        xs = cycle(xs)
        ans = 0
        for x, y in xs:
            ans += height - y
        A[i] = ans

    fi = A[STOP]
    k = None
    for i in range(STOP + 1, STOP * 2):
        if A[i] == fi:
            k = i - STOP
            break
    assert k is not None
    return A[STOP + ((1000000000 - STOP) % k)]


print(part1())
print(part2())
