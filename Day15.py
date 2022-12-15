import re

with open('inputs/day15.txt') as f:
    lines = f.read().strip().split('\n')
    coords = []
    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        coords.append(((sx, sy), (bx, by)))

def manhattan(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

ROW = 2000000 # 10

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

def merge_intervals(intervals):
    if len(intervals) == 0:
        return []
    merged = []
    intervals.sort()
    prev = intervals[0]
    for interval in intervals[1:]:
        if interval[0] <= prev[1] + 1:
            prev = prev[0], max(prev[1], interval[1])
        else:
            merged.append(prev)
            prev = interval
    merged.append(prev)
    return merged

max_coord = 4000000 # 20
for y in range(max_coord):
    intervals = []
    for (sensor, beacon) in coords:
        distance = manhattan(*sensor, *beacon)
        dy = abs(sensor[1] - y)
        if dy <= distance:
            width = distance - dy
            intervals.append((sensor[0] - width, sensor[0] + width))
    merged = merge_intervals(intervals)
    if len(merged) == 2:
        x = min(merged[0][1], merged[1][1]) + 1
        print(x * 4000000 + y)
        break
