import numpy as np

from utils.input import aoc

ip = aoc(2023, 21)
L = [l for l in ip.splitlines()]
width, height = len(L[0]), len(L)

D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sx = sy = 0
for x, row in enumerate(L):
    for y, c in enumerate(row):
        if c == "S":
            sx, sy = (x, y)


def step(G, C):
    S = set()
    for x, y in C:
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(G[0]) and 0 <= ny < len(G) and G[ny][nx] != '#':
                S.add((nx, ny))
    return S


def tile(G, n):
    return [row * n for row in G * n]


def part1():
    C = {(sx, sy)}
    for i in range(64):
        C = step(L, C)
    return len(C)


def part2():
    k = 16
    C = {(sx + k * width // 2, sy + k * height // 2)}

    A = []
    for i in range(26501365):
        if i % width == 65:
            A.append(len(C))
            if len(A) == 3:
                break
        C = step(tile(L, k), C)

    a, b, c = map(round, np.polyfit([0, 1, 2], A, 2))
    return a * 202300 ** 2 + b * 202300 + c


print(part1())
print(part2())
