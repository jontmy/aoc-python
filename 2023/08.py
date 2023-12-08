import itertools
import math
import re

from utils.input import aoc

ip = aoc(2023, 8)
steps, rest = [line for line in ip.split("\n\n")]
lines = [re.findall(r"\w+", ls) for ls in rest.splitlines()]
ins = {a: (l, r) for a, l, r in lines}


def part1():
    c = 'AAA'
    ans = 0
    for d in itertools.cycle(steps):
        if c == 'ZZZ':
            break
        if d == 'L':
            c = ins[c][0]
        elif d == 'R':
            c = ins[c][1]
        else:
            assert False
        ans += 1
    return ans


def part2():
    A = []
    xs = [x for x in ins if x[-1] == 'A']
    for x in xs:
        i = 0
        B = []
        for d in itertools.cycle(steps):
            if x[-1] == 'Z':
                B.append(i)
            if len(B) == 2:
                break
            if d == 'L':
                x = ins[x][0]
            elif d == 'R':
                x = ins[x][1]
            else:
                assert False
            i += 1
        A.append(B)
    return math.lcm(*[y - x for x, y in A])


print(part1())
print(part2())
