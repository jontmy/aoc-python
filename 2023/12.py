from functools import cache
from utils.input import aoc

ip = aoc(2023, 12)
lines = [line.split(" ") for line in ip.splitlines()]
lines = [(tuple(xs), tuple(map(int, ys.split(",")))) for xs, ys in lines]


@cache
def combinations(xs, ys):
    if not ys:
        if '#' in xs:
            return 0
        else:
            return 1

    if sum(ys) > len(xs):
        return 0

    if xs[0] == '.':
        return combinations(xs[1:], ys)

    ans = 0
    if xs[0] == '?':
        ans += combinations(xs[1:], ys)

    if '.' in xs[:ys[0]]:
        return ans

    if len(xs) > ys[0] and xs[ys[0]] == '#':
        return ans

    ans += combinations(xs[(ys[0] + 1):], ys[1:])
    return ans


def solve(lines):
    return sum(combinations(xs, ys) for xs, ys in lines)


def part1():
    return solve(lines)


def part2():
    return solve((((*xs, '?') * 5)[:-1], ys * 5) for xs, ys in lines)


assert combinations(tuple('?'), (1,)) == 1
assert combinations(tuple('??'), (1,)) == 2
assert combinations(tuple('??.?'), (1, 1)) == 2
assert combinations(tuple('??.??'), (1,)) == 4
assert combinations(tuple('??.??'), (1, 1)) == 4
assert combinations(tuple('??.??'), (1, 2)) == 2
assert combinations(tuple('??#??'), (5,)) == 1
assert combinations(tuple('?#?#?'), (2, 2)) == 1
assert combinations(tuple('?#?#?#'), (2, 3)) == 1
assert combinations(tuple('?#?#?#?'), (1, 3)) == 1
assert combinations(tuple('.##.?#??.#.?#'), (2, 1, 1, 1)) == 1

print(part1())
print(part2())
