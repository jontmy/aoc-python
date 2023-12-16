import sys

from utils.input import aoc

ip = aoc(2023, 16)
G = ip.splitlines()
width, height = len(G[0]), len(G)
sys.setrecursionlimit(10 ** 6)


def energize(x: int, y: int, dx: int, dy: int, V: set, C: set) -> int:
    if not (0 <= x < width and 0 <= y < height):
        return len(V)
    V.add((x, y))
    if (x, y, dx, dy) in C:
        return len(V)
    C.add((x, y, dx, dy))
    match G[y][x]:
        case '.':
            energize(x + dx, y + dy, dx, dy, V, C)
        case '/':
            match (dx, dy):
                case (-1, 0):
                    energize(x, y + 1, 0, 1, V, C)
                case (0, -1):
                    energize(x + 1, y, 1, 0, V, C)
                case (1, 0):
                    energize(x, y - 1, 0, -1, V, C)
                case (0, 1):
                    energize(x - 1, y, -1, 0, V, C)
        case "\\":
            match (dx, dy):
                case (1, 0):
                    energize(x, y + 1, 0, 1, V, C)
                case (0, -1):
                    energize(x - 1, y, -1, 0, V, C)
                case (-1, 0):
                    energize(x, y - 1, 0, -1, V, C)
                case (0, 1):
                    energize(x + 1, y, 1, 0, V, C)
        case '|':
            match (dx, dy):
                case (0, 1), (0, -1):
                    energize(x, y + dy, dx, dy, V, C)
                case _:
                    energize(x, y + 1, 0, 1, V, C)
                    energize(x, y - 1, 0, -1, V, C)
        case '-':
            match (dx, dy):
                case (1, 0), (-1, 0):
                    energize(x + dx, y, dx, dy, V, C)
                case _:
                    energize(x + 1, y, 1, 0, V, C)
                    energize(x - 1, y, -1, 0, V, C)
    return len(V)


def part1():
    return energize(0, 0, 1, 0, set(), set())


def part2():
    ans = 0
    for x in range(width):
        ans = max(ans, energize(x, 0, 0, 1, set(), set()), energize(x, height - 1, 0, -1, set(), set()))
    for y in range(height):
        ans = max(ans, energize(0, y, 1, 0, set(), set()), energize(width - 1, y, -1, 0, set(), set()))
    return ans


print(part1())
print(part2())
