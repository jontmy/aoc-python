import networkx

from utils.input import aoc

ip = aoc(2023, 25)
L = [l.split(": ") for l in ip.splitlines()]
L = [(l[0], l[1].split(" ")) for l in L]


def solve():
    G = networkx.Graph()
    V = set()

    for u, vs in L:
        V.add(u)
        for v in vs:
            G.add_edge(u, v, capacity=1)
            V.add(v)

    V = list(V)
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            sz, (xs, ys) = networkx.minimum_cut(G, V[i], V[j])
            if sz == 3:
                return len(xs) * len(ys)


print(solve())
