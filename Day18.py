from itertools import product
from queue import SimpleQueue

with open('inputs/day18.txt') as f:
    cubes = [tuple(map(int, line.split(','))) for line in f.read().strip().split()]

adjacent = [
    (0, 0, 1),
    (1, 0, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1)
]

def simple_area(cubes):
    sides = {}
    for cube in cubes:
        x, y, z = cube
        left = 6
        for (dx, dy, dz) in adjacent:
            other = x + dx, y + dy, z + dz
            if other in sides:
                sides[other] -= 1
                left -= 1
        sides[cube] = left

    return sum(sides.values())

print(simple_area(cubes))

space = set()
q = SimpleQueue()

max_x = max(cubes, key=lambda cube: cube[0])[0] + 1
min_x = min(cubes, key=lambda cube: cube[0])[0] - 1
max_y = max(cubes, key=lambda cube: cube[1])[1] + 1
min_y = min(cubes, key=lambda cube: cube[1])[1] - 1
max_z = max(cubes, key=lambda cube: cube[2])[2] + 1
min_z = min(cubes, key=lambda cube: cube[2])[2] - 1

q.put((min_x, min_y, min_z))
while not q.empty():
    cube = q.get()
    if cube not in space:
        space.add(cube)
        (x, y, z) = cube
        for dx, dy, dz in adjacent:
            other = x + dx, y + dy, z + dz
            if min_x <= other[0] <= max_x and min_y <= other[1] <= max_y and min_z <= other[2] <= max_z:
                if other not in cubes:
                    q.put(other)

inverse_area = simple_area(space)
w, h, d = max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1
outer_area = 2 * (w * h + w * d + h * d)
print(inverse_area - outer_area)
