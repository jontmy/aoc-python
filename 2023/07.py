import itertools
from collections import Counter

from utils.input import aoc

ip = aoc(2023, 7)
lines = [line.split(' ') for line in ip.splitlines()]

vals1 = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    "A": 14,
}

vals2 = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    "A": 14,
}


def strength1(cards):
    ss = set(cards)
    cs = Counter(cards)
    if len(ss) == 5:
        # high card
        return 1
    if len(ss) == 4:
        # one pair
        return 2
    if len(ss) == 3:
        if 3 in cs.values():
            # three of a kind
            return 4
        else:
            # two pair
            return 3
    if len(ss) == 2:
        if 4 in cs.values():
            # four of a kind
            return 6
        else:
            # full house
            return 5
    if len(ss) == 1:
        # five of a kind
        return 7
    assert False


def strength2(cards):
    if 'J' not in cards:
        return strength1(cards)
    xs = [c for c in cards if c != 'J']
    subs = [c for c in vals2.keys() if c != 'J']
    return max([strength1([*xs, *ys]) for ys in itertools.combinations_with_replacement(subs, 5 - len(xs))])


def cmp1(ls):
    xs = ls[0]
    return strength1(xs), *[vals1[x] for x in xs]


def cmp2(ls):
    xs = ls[0]
    return strength2(xs), *[vals2[x] for x in xs]


def part1():
    ans = 0
    cards = sorted(lines, key=cmp1)
    for i, l in enumerate(cards):
        ans += (i + 1) * int(l[1])
    return ans


def part2():
    ans = 0
    cards = sorted(lines, key=cmp2)
    for i, l in enumerate(cards):
        ans += (i + 1) * int(l[1])
    return ans


print(part1())
print(part2())
