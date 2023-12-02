from utils.input import aoc

ip = aoc(2023, 2)
ip1 = ip
ip2 = ip

p1 = 0
p2 = 0

for line in ip.splitlines():
    guid, rest = line.split(':')
    uid = int(guid.split(" ")[-1])
    xs = rest.split("; ")

    possible = True
    for x in xs:
        ys = [y.strip().split(" ") for y in x.split(", ")]
        for count, color in ys:
            count = int(count)
            if color == 'red' and count > 12:
                possible = False
            elif color == 'green' and count > 13:
                possible = False
            elif color == 'blue' and count > 14:
                possible = False
    if possible:
        p1 += uid

for line in ip.splitlines():
    guid, rest = line.split(':')
    uid = int(guid.split(" ")[-1])
    xs = rest.split("; ")

    r, g, b, = 0, 0, 0
    for x in xs:
        ys = [y.strip().split(" ") for y in x.split(", ")]
        for count, color in ys:
            count = int(count)
            if color == 'red':
                r = max(r, count)
            elif color == 'green':
                g = max(g, count)
            elif color == 'blue':
                b = max(b, count)
    p2 += r * g * b

print(p1)
print(p2)
