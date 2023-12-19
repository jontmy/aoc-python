import re

from math import prod
from utils.input import aoc

ip = aoc(2023, 19)
W, P = [g for g in ip.split("\n\n")]

R = {k: [tuple(u.split(":")) for u in v.split(",")] for k, v in re.findall(r"(\w+){(.*?),\w+}", W)}
DR = {k: v for k, v in re.findall(r"(\w+){.*?,(\w+)}", W)}
P = [tuple(map(int, re.findall(r"\d+", p))) for p in P.split()]


def part1():
    ans = 0
    for x, m, a, s in P:
        cr = 'in'
        while True:
            if cr == 'A':
                ans += x + m + a + s
                break
            elif cr == 'R':
                break
            for r, nr in R[cr]:
                if eval(r):
                    cr = nr
                    break
            else:
                cr = DR[cr]
    return ans


def split(r, xmas):
    c, op, k = r[0], r[1], int(r[2:])
    T = {k: v if k != c else [] for k, v in xmas.items()}
    F = {k: v if k != c else [] for k, v in xmas.items()}
    if op == '<':
        for start, end in xmas[c]:
            if start > k:
                F[c].append((start, end))
            elif end < k:
                T[c].append((start, end))
            else:
                assert start <= k <= end
                T[c].append((start, k))
                F[c].append((k, end))
    elif op == '>':
        for start, end in xmas[c]:
            if start > k:
                T[c].append((start, end))
            elif end < k:
                F[c].append((start, end))
            else:
                T[c].append((k + 1, end))
                F[c].append((start, k + 1))
    else:
        assert False
    return T, F


def size(xmas):
    return prod(sum(end - start for start, end in xs) for xs in xmas.values())


def solve(cr, xmas):
    if cr == 'A':
        return size(xmas)
    elif cr == 'R':
        return 0
    a = 0
    for r, nr in R[cr]:
        T, F = split(r, xmas)
        a += solve(nr, T)
        xmas = F
    return a + solve(DR[cr], xmas)


def part2():
    return solve('in', {
        'x': [(1, 4001)],
        'm': [(1, 4001)],
        'a': [(1, 4001)],
        's': [(1, 4001)],
    })


print(part1())
print(part2())
