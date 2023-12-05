import itertools
from collections import defaultdict

from utils.input import aoc

ip = aoc(2023, 5)
[seeds, *_maps] = [g for g in ip.split("\n\n")]
seeds = [int(s) for s in seeds.split(": ")[-1].split(" ")]
maps = defaultdict(list)
convs = dict()

for m in _maps:
    a, *rest = m.splitlines()
    i, o = a.split(" ")[0].split("-to-")
    convs[i] = o
    for r in rest:
        maps[(i, o)].append(tuple(map(int, r.split(" "))))


def part1():
    possible = []
    for seed in seeds:
        curr_type = 'seed'
        curr_value = seed
        while curr_type != 'location':
            next_type = convs[curr_type]
            ranges = maps[(curr_type, next_type)]
            for dst, src, l in ranges:
                if src <= curr_value < src + l:
                    curr_value = dst + curr_value - src
                    break
            curr_type = next_type
        possible.append(curr_value)
    ans = min(possible)
    return ans


def part2():
    # brute forced
    ans = 0
    unconvs = {v: k for k, v in convs.items()}
    seed_ranges = [(seed, seed + seeds[i + 1]) for i, seed in enumerate(seeds) if i % 2 == 0]

    while True:
        curr_type = 'location'
        curr_value = ans
        while curr_type != 'seed':
            prev_type = unconvs[curr_type]
            for dst, src, l in maps[(prev_type, curr_type)]:
                if dst <= curr_value < dst + l:
                    curr_value = src + curr_value - dst
                    break
            curr_type = prev_type

        for start, end in seed_ranges:
            if start <= curr_value < end:
                return ans
        ans += 1


print(part1())
print(part2())
