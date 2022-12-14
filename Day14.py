from itertools import pairwise

with open('inputs/day14.txt') as f:
    lines = f.read().strip().split('\n')

rocks = set()

for line in lines:
    coords = [coord.split(',') for coord in line.split(' -> ')]
    coords = [(int(x), int(y)) for [x, y] in coords]
    for (x0, y0), (x1, y1) in pairwise(coords):
        dx, dy = x1 - x0, y1 - y0
        if dx == 0:
            dy = 1 if dy > 0 else -1
        else:
            dx = 1 if dx > 0 else -1
        while (x0, y0) != (x1, y1):
            rocks.add((x0, y0))
            x0, y0 = x0 + dx, y0 + dy
        rocks.add((x1, y1))

rocks2 = rocks.copy()
lowest_y = max((rock[1] for rock in rocks))

def fall():
    x, y = 500, 0
    while y < lowest_y:
        if (x, y + 1) not in rocks:
            y += 1
        else:
            if (x - 1, y + 1) not in rocks:
                x, y = x - 1, y + 1
            elif (x + 1, y + 1) not in rocks:
                x, y = x + 1, y + 1
            else:
                rocks.add((x, y))
                return True
    return False

part1 = 0
while fall():
    part1 += 1

print(part1)

floor = lowest_y + 2

def fall_floor():
    x, y = 500, 0
    while True:
        if y == floor - 1:
            rocks2.add((x, y))
            return True
        elif (x, y + 1) not in rocks2:
            y += 1
        else:
            if (x - 1, y + 1) not in rocks2:
                x, y = x - 1, y + 1
            elif (x + 1, y + 1) not in rocks2:
                x, y = x + 1, y + 1
            else:
                if (x, y) == (500, 0):
                    return False
                rocks2.add((x, y))
                return True

part2 = 1
while fall_floor():
    part2 += 1

print(part2)
