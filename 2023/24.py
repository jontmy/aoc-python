import re

from utils.input import aoc
from z3 import *

ip = aoc(2023, 24)
L = [list(map(int, re.findall(r"-?\d+", line))) for line in ip.splitlines()]

min_x = min_y = 200000000000000
max_x = max_y = 400000000000000


# Source: https://stackoverflow.com/a/20677983

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def part1():
    ans = 0
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            x1, y1, z1, dx1, dy1, dz1 = L[i]
            x2, y2, z2, dx2, dy2, dz2 = L[j]
            int = line_intersection(((x1, y1), (x1 + dx1, y1 + dy1)), ((x2, y2), (x2 + dx2, y2 + dy2)))
            if not int:
                continue
            x, y = int
            if min_x <= x <= max_x and min_y <= y <= max_y:
                if dx1 < 0 and x > x1:
                    continue
                if dx1 > 0 and x < x1:
                    continue
                if dx2 < 0 and x > x2:
                    continue
                if dx2 > 0 and x < x2:
                    continue
                if dy1 < 0 and y > y1:
                    continue
                if dy1 > 0 and y < y1:
                    continue
                if dy2 < 0 and y > y2:
                    continue
                if dy2 > 0 and y < y2:
                    continue
                ans += 1
    return ans


def part2():
    x, y, z = Real('x'), Real('y'), Real('z')
    dx, dy, dz = Real('dx'), Real('dy'), Real('dz')
    S = Solver()

    for i, l in enumerate(L):
        t = Real(f't{i}')
        S.add(t >= 0)
        S.add(x + dx * t == l[0] + l[3] * t)
        S.add(y + dy * t == l[1] + l[4] * t)
        S.add(z + dz * t == l[2] + l[5] * t)

    if S.check() != sat:
        assert False

    m = S.model()
    return m[x].as_long() + m[y].as_long() + m[z].as_long()


print(part1())
print(part2())
