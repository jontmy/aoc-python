import re
from utils.input import aoc

ip = aoc(2023, 9)
lines = [list(map(int, re.findall(r"-?\d+", line))) for line in ip.splitlines()]


def ext1(xs):
    a = xs[-1]
    while any(x != 0 for x in xs):
        xs = [b - a for b, a in zip(xs[1:], xs)]
        a += xs[-1]
    return a


def ext2(xs):
    A, a = [xs[0]], 0
    while any(x != 0 for x in xs):
        xs = [b - a for b, a in zip(xs[1:], xs)]
        A.append(xs[0])
    for x in reversed(A):
        a = -a + x
    return a


def part1():
    return sum(ext1(xs) for xs in lines)


def part2():
    return sum(ext2(xs) for xs in lines)


print(part1())
print(part2())
