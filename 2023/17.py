import networkx
from utils.input import aoc

ip = aoc(2023, 17)
lines = [list(map(int, line)) for line in ip.splitlines()]
width, height = len(lines[0]), len(lines)


def flatten(xs):
    return [y for ys in xs for y in ys]


def D(d_min, d_max):
    return flatten([
        [(0, -k, 'N') for k in range(d_min, d_max + 1)],
        [(0, k, 'S') for k in range(d_min, d_max + 1)],
        [(k, 0, 'E') for k in range(d_min, d_max + 1)],
        [(-k, 0, 'W') for k in range(d_min, d_max + 1)]
    ])


def weight(u, v):
    x, y, d = u
    nx, ny, nd = v
    match nd:
        case 'N':
            return sum(lines[j][x] for j in range(ny, y))
        case 'S':
            return sum(lines[j][x] for j in range(y + 1, ny + 1))
        case 'E':
            return sum(lines[y][i] for i in range(x + 1, nx + 1))
        case 'W':
            return sum(lines[y][i] for i in range(nx, x))
    assert False


def solve(d_min, d_max):
    G = networkx.DiGraph()
    for d in ['N', 'S', 'E', 'W']:
        G.add_edge((0, 0), (0, 0, d), weight=0)
        G.add_edge((width - 1, height - 1, d), (width - 1, height - 1), weight=0)

    for y in range(height):
        for x in range(width):
            for d in ['N', 'S', 'E', 'W']:
                for dx, dy, nd in D(d_min, d_max):
                    if d == nd or (d, nd) in [('N', 'S'), ('S', 'N'), ('E', 'W'), ('W', 'E')]:
                        continue
                    u = x, y, d
                    v = nx, ny, nd = x + dx, y + dy, nd
                    if not (0 <= nx < width and 0 <= ny < height):
                        continue
                    G.add_edge((x, y, d), (nx, ny, nd), weight=weight(u, v))

    return networkx.single_source_dijkstra(G, (0, 0), (width - 1, height - 1))[0]


print(solve(1, 3))
print(solve(4, 10))
