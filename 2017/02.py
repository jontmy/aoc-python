import re

from utils.input import aoc

ip = aoc(2017, 2)
ip = [[int(x) for x in re.split("\t", l)] for l in ip.splitlines()]

p1 = sum(max(xs) - min(xs) for xs in ip)
p2 = 0

for xs in ip:
    for i in range(len(xs)):
        for j in range(len(xs)):
            if i == j:
                continue
            if xs[i] % xs[j] == 0:
                p2 += xs[i] // xs[j]

print(p1)
print(p2)
