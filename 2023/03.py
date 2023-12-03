import re
from utils.input import aoc

ip = aoc(2023, 3)
lines = [line for line in ip.splitlines()]
dirs = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1)]


def part1():
    ans = 0
    symbols = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if not c.isdigit() and c != '.':
                symbols.add((x, y))

    nums = []
    for y, line in enumerate(lines):
        for m in re.finditer('\\d+', line):
            nums.append((int(m.group()), m.start(), m.end(), y))

    for num, min_x, max_x, y in nums:
        ok = False
        for x in range(min_x, max_x):
            for dx, dy in dirs:
                if (x + dx, y + dy) in symbols:
                    ok = True
        if ok:
            ans += num

    return ans


def part2():
    ans = 0
    symbols = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '*':
                symbols.add((x, y))

    nums = []
    for y, line in enumerate(lines):
        for m in re.finditer('\\d+', line):
            nums.append((int(m.group()), m.start(), m.end(), y))

    for (x, y) in symbols:
        adj = set()
        for dx, dy in dirs:
            for num, min_x, max_x, ny in nums:
                for nx in range(min_x, max_x):
                    if nx == x + dx and ny == y + dy:
                        adj.add(num)
        if len(adj) == 2:
            a, b = list(adj)
            ans += a * b

    return ans


print(part1())
print(part2())
