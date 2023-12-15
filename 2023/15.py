from collections import defaultdict

from utils.input import aoc

ip = aoc(2023, 15)
ip = ip.split(",")


def _hash(g):
    h = 0
    for c in g:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def part1():
    return sum(map(_hash, ip))


def part2():
    D = defaultdict(dict)
    for g in ip:
        label = g[:-1] if g[-1] == "-" else g[:-2]
        op = g[-1] if g[-1] == "-" else g[-2]
        box = _hash(label)
        if op == "-":
            if label in D[box]:
                del D[box][label]
        elif op == '=':
            D[box][label] = g[-1]
        else:
            assert False

    ans = 0
    for k, v in D.items():
        for i, x in enumerate(v.values()):
            ans += (k + 1) * (i + 1) * int(x)
    return ans


print(part1())
print(part2())
