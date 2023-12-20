import itertools
import math

from collections import defaultdict, deque
from utils.input import aoc

ip = aoc(2023, 20)
L = [l.split(" -> ") for l in ip.splitlines()]

A = dict()
R = defaultdict(lambda: ("?", []))
TARGET = None

for a, b in L:
    c, inp, out = a[0], a[1:], b.split(", ")
    if 'rx' in out:
        TARGET = inp
    if c == '%':
        R[inp] = (c, out)
    elif c == '&':
        R[inp] = (c, out)
        A[inp] = dict()
    else:
        R["broadcaster"] = ("broadcaster", out)

assert TARGET is not None
for inp, (_, out) in R.items():
    for o in out:
        if o in A:
            A[o][inp] = False


def step(P, Q, pn, cv, cn):
    ct, nns = R[cn]
    match ct, cv:
        case "broadcaster", _:
            Q.extend((cn, P[cn], nn) for nn in nns)
        case "%", False:
            P[cn] = not P[cn]
            Q.extend((cn, P[cn], nn) for nn in nns)
        case "&", _:
            A[cn][pn] = cv
            Q.extend((cn, not all(A[cn].values()), nn) for nn in nns)


def part1():
    P = defaultdict(bool)
    lo = hi = 0
    for i in range(1000):
        Q = deque([("button", False, "broadcaster")])
        while Q:
            pn, cv, cn = Q.popleft()
            step(P, Q, pn, cv, cn)
            if cv:
                hi += 1
            else:
                lo += 1
    return lo * hi


def part2():
    P = defaultdict(bool)
    cycles = dict()
    for i in itertools.count():
        Q = deque([("button", False, "broadcaster")])
        while Q:
            pn, cv, cn = Q.popleft()
            step(P, Q, pn, cv, cn)
            if cn == TARGET and cv and pn not in cycles:
                cycles[pn] = i
                if len(cycles) == 4:
                    return math.lcm(*[a + 1 for a in cycles.values()])


print(part1())
print(part2())
