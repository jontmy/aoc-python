from utils.input import aoc

ip = aoc(2023, 13)
groups = [[list(xs) for xs in line.split()] for line in ip.split("\n\n")]


def _solve(G, k=1):
    return set(
        x * k
        for x in range(1, len(G[0]))
        if all(all(l == r for l, r in zip(reversed(row[:x]), row[x:])) for row in G)
    )


def solve(G):
    return _solve(G) | _solve(list(map(list, zip(*G))), 100)


def part1():
    return sum(next(iter(solve(G))) for G in groups)


def part2():
    ans = 0
    for G in groups:
        s = set()
        for y in range(len(G)):
            for x in range(len(G[0])):
                G[y][x] = '#' if G[y][x] == '.' else '.'
                s |= solve(G)
                G[y][x] = '#' if G[y][x] == '.' else '.'
        s.discard(0)
        s -= solve(G)
        ans += next(iter(s))
    return ans


print(part1())
print(part2())
