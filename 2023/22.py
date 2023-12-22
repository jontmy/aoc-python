import re
from collections import defaultdict

from utils.input import aoc

ip = aoc(2023, 22)
L = [line for line in ip.splitlines()]
D = defaultdict(set)

ASCII = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def key(x, y, z, DND):
    for k, v in DND.items():
        if (x, y, z) in v:
            # return ASCII[k]
            return str(k)
    return '.'


def part1():
    xi, xj = 0, 0
    yi, yj = 0, 0
    zi, zj = 0, 0

    for i, l in enumerate(L):
        x1, y1, z1, x2, y2, z2 = map(int, re.findall(r'\d+', l))

        min_x, max_x = min(x1, x2), max(x1, x2)
        xi = min(xi, min_x)
        xj = max(xj, max_x)

        min_y, max_y = min(y1, y2), max(y1, y2)
        yi = min(yi, min_y)
        yj = max(yj, max_y)

        min_z, max_z = min(z1, z2), max(z1, z2)
        zi = min(zi, min_z)
        zj = max(zj, max_z)

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    D[i].add((x, y, z))

    # falling
    assert xi == yi == zi == 0
    S = set(D.keys())
    G = [[1 for y in range(yi, yj + 1)] for x in range(xi, xj + 1)]
    ND = defaultdict(set)
    while S:
        min_z = zj + 1
        min_s = None
        for s in S:
            if all(z < min_z for x, y, z in D[s]):
                min_z = min(z for x, y, z in D[s])
                min_s = s

        max_z = 0
        max_dz = zj + 1
        assert max_dz >= 0

        for x, y, z in D[min_s]:
            assert z >= G[x][y]
            max_z = max(max_z, z)
            max_dz = min(max_dz, z - G[x][y])

        for x, y, z in D[min_s]:
            G[x][y] = max(G[x][y], max_z - max_dz + 1)
            ND[min_s].add((x, y, z - max_dz))

        S.remove(min_s)

    # disintegration
    assert len(D) == len(ND)
    ans = 0
    for s, rm in ND.items():
        max_z = max(z for x, y, z in rm)
        spt = set()
        # find supporting bricks
        for t, xs in ND.items():
            if s == t:
                continue
            for x, y, z in xs:
                if z == max_z:
                    spt.add((x, y, z))
        # check if any falls
        ok = True
        for t, xs in ND.items():
            if s == t:
                continue
            # must have at least 1 cube directly above the brick to be disintegrated
            if not any((x, y, z + 1) in xs for x, y, z in rm):
                continue
            # fall only if no supporting bricks
            if not any((x, y, z - 1) in spt for x, y, z in xs):
                ok = False
        if ok:
            ans += 1

    return ans


def part2():
    xi, xj = 0, 0
    yi, yj = 0, 0
    zi, zj = 0, 0

    for i, l in enumerate(L):
        x1, y1, z1, x2, y2, z2 = map(int, re.findall(r'\d+', l))

        min_x, max_x = min(x1, x2), max(x1, x2)
        xi = min(xi, min_x)
        xj = max(xj, max_x)

        min_y, max_y = min(y1, y2), max(y1, y2)
        yi = min(yi, min_y)
        yj = max(yj, max_y)

        min_z, max_z = min(z1, z2), max(z1, z2)
        zi = min(zi, min_z)
        zj = max(zj, max_z)

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    D[i].add((x, y, z))

    # falling
    assert xi == yi == zi == 0
    S = set(D.keys())
    G = [[1 for y in range(yi, yj + 1)] for x in range(xi, xj + 1)]
    ND = defaultdict(set)
    while S:
        min_z = zj + 1
        min_s = None
        for s in S:
            if all(z < min_z for x, y, z in D[s]):
                min_z = min(z for x, y, z in D[s])
                min_s = s

        max_z = 0
        max_dz = zj + 1
        assert max_dz >= 0

        for x, y, z in D[min_s]:
            assert z >= G[x][y]
            max_z = max(max_z, z)
            max_dz = min(max_dz, z - G[x][y])

        for x, y, z in D[min_s]:
            G[x][y] = max(G[x][y], max_z - max_dz + 1)
            ND[min_s].add((x, y, z - max_dz))

        S.remove(min_s)

    # disintegration
    assert len(D) == len(ND)
    ans = 0
    for s, rm in ND.items():
        max_z = max(z for x, y, z in rm)
        spt = set()
        # find supporting bricks
        for t, xs in ND.items():
            if s == t:
                continue
            for x, y, z in xs:
                if z == max_z:
                    spt.add((x, y, z))
        # check if any falls
        ok = True
        for t, xs in ND.items():
            if s == t:
                continue
            # must have at least 1 cube directly above the brick to be disintegrated
            if not any((x, y, z + 1) in xs for x, y, z in rm):
                continue
            # fall only if no supporting bricks
            if not any((x, y, z - 1) in spt for x, y, z in xs):
                ok = False

        if not ok:
            # falling
            assert xi == yi == zi == 0
            T = set(t for t in D.keys() if t != s)
            G = [[1 for y in range(yi, yj + 1)] for x in range(xi, xj + 1)]
            NND = defaultdict(set)
            while T:
                min_z = zj + 1
                min_t = None
                for t in T:
                    if all(z < min_z for x, y, z in D[t]):
                        min_z = min(z for x, y, z in D[t])
                        min_t = t

                max_z = 0
                max_dz = zj + 1
                assert max_dz >= 0

                for x, y, z in D[min_t]:
                    assert z >= G[x][y]
                    max_z = max(max_z, z)
                    max_dz = min(max_dz, z - G[x][y])

                for x, y, z in D[min_t]:
                    G[x][y] = max(G[x][y], max_z - max_dz + 1)
                    NND[min_t].add((x, y, z - max_dz))

                if tuple(sorted(NND[min_t])) != tuple(sorted(ND[min_t])):
                    ans += 1

                T.remove(min_t)

    return ans


print(part1())
print(part2())
