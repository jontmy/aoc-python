from utils.input import aoc

ip = aoc(2023, 18)
L = [l.split() for l in ip.splitlines()]
D = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
    '0': (1, 0),
    '1': (0, 1),
    '2': (-1, 0),
    '3': (0, -1),
}


def area(V):
    return abs(sum(ax * by - bx * ay for (ax, ay), (bx, by) in zip(V, [*V[1:], V[0]]))) // 2


def solve(part):
    V = [(0, 0)]
    t = 2
    for d, k, h in L:
        d = h[-2] if part == 2 else d
        k = int(h[2:-2], 16) if part == 2 else int(k)
        t += k
        V.append((V[-1][0] + D[d][0] * k, V[-1][1] + D[d][1] * k))
    return area(V) + t // 2


print(solve(part=1))
print(solve(part=2))
