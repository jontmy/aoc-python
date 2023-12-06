import re

from utils.input import aoc

ip = aoc(2023, 6)
t1, d1 = [[int(x) for x in re.findall(r"\d+", line)] for line in ip.splitlines()]
t2, d2 = [int(''.join(list(map(str, t1))))], [int(''.join(list(map(str, d1))))]


def solve(ts, ds):
    ans = 1
    for t, d in zip(ts, ds):
        a = 0
        for i in range(t):
            r = t - i
            if r * i > d:
                a += 1
        ans *= a
    return ans


print(solve(t1, d1))
print(solve(t2, d2))
