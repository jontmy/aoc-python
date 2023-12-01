import re
from utils.input import aoc

ip = aoc(2023, 1)
ip1 = ip
ip2 = ip

p1 = 0
p2 = 0

for line in ip.splitlines():
    xs = [x for x in line if x in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}]
    p1 += int(xs[0] + xs[-1])

for line in ip.splitlines():
    xs = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    d = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '0': '0'
    }
    p2 += int(d[xs[0]] + d[xs[-1]])

print(p1)
print(p2)
