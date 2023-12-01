from utils.input import aoc

ip = aoc(2017, 1)
ip1 = ip + ip[0]

p1 = 0
p2 = 0

for i in range(len(ip1) - 1):
    if ip1[i] == ip1[i + 1]:
        p1 += int(ip1[i])

skip = len(ip) // 2
ip2 = ip + ip[:skip]
for i in range(len(ip2) - skip):
    if ip2[i] == ip2[i + skip]:
        p2 += int(ip2[i])

print(p1)
print(p2)
