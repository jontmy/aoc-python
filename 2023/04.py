from utils.input import aoc

ip = aoc(2023, 4)
lines = [line for line in ip.splitlines()]


def part1():
    ans = 0
    for line in lines:
        _, rest = line.split(": ")
        xs, ys = [set(l for l in ls.split(" ") if len(l)) for ls in rest.split(" | ")]
        matches = xs & ys
        if len(matches):
            ans += 2 ** (len(matches) - 1)
    return ans


def part2():
    ans = 0
    matches = dict()
    for line in lines:
        uid, rest = line.split(": ")
        uid = int(uid.split(" ")[-1])
        xs, ys = [set(l for l in ls.split(" ") if len(l)) for ls in rest.split(" | ")]
        matches[uid] = len(xs & ys)

    proc = [i for i in matches.keys()]
    while proc:
        curr = proc.pop()
        ans += 1
        ext = [curr + x + 1 for x in range(matches[curr])]
        proc += ext

    return ans


print(part1())
print(part2())
