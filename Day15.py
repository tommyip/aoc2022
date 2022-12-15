import re

with open('inputs/day15.txt') as f:
    lines = f.read().strip().split('\n')
    coords = []
    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        coords.append(((sx, sy), (bx, by)))

def manhattan(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

ROW = 2000000

pos = set()
for (sensor, beacon) in coords:
    distance = manhattan(*sensor, *beacon)
    height = abs(sensor[1] - ROW)
    if height <= distance:
        width = distance - height
        x = sensor[0]
        pos.update(range(x, x + width + 1))
        pos.update(range(x - width, x))
for (_, (x, y)) in coords:
    if y == ROW and x in pos:
        pos.remove(x)

print(len(pos))
