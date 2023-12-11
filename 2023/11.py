from utils.input import aoc

ip = aoc(2023, 11)
lines = [line for line in ip.splitlines()]
height, width = len(lines), len(lines[0])


def solve(k):
    exp_ys = [y for y, row in enumerate(lines) if all(c == '.' for c in row)]
    exp_xs = [x for x in range(width) if all(lines[y][x] == '.' for y in range(height))]

    G = []
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c != '#':
                continue
            dx = len([exp_x for exp_x in exp_xs if exp_x < x])
            dy = len([exp_y for exp_y in exp_ys if exp_y < y])
            G.append((x + dx * (k - 1), y + dy * (k - 1)))

    ans = 0
    for i in range(len(G)):
        for j in range(i, len(G)):
            (x1, y1), (x2, y2) = G[i], G[j]
            ans += abs(x1 - x2) + abs(y1 - y2)
    return ans


print(solve(2))
print(solve(1000000))
