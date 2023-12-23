import networkx

from utils.input import aoc

D = {
    "v": [(0, 1)],
    ">": [(1, 0)],
    "^": [(0, -1)],
    "<": [(-1, 0)],
    '.': [(-1, 0), (1, 0), (0, -1), (0, 1)],
    '#': []
}


def solve(part):
    ip = aoc(2023, 23)
    if part == 2:
        ip = ip.replace('>', '.')
        ip = ip.replace('<', '.')
        ip = ip.replace('^', '.')
        ip = ip.replace('v', '.')

    G = networkx.DiGraph()
    L = [list(l) for l in ip.splitlines()]
    width, height = len(L[0]), len(L)

    for y, row in enumerate(L):
        for x, c in enumerate(row):
            for dx, dy in D[c]:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < width or not 0 <= ny < height:
                    continue
                if L[ny][nx] == '#':
                    continue
                G.add_edge((x, y), (nx, ny))

    ans = 0
    for sp in networkx.all_simple_paths(G, source=(1, 1), target=(width - 2, height - 1)):
        ans = max(ans, len(sp))
        if part == 2:
            # let it run for ~2 hours and submit
            # TODO: optimize this
            print(ans)
    return ans


print(solve(part=1))
print(solve(part=2))
