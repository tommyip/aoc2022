from collections import Counter

with open('inputs/day23.txt') as f:
    lines = f.read().strip().split('\n')
    elfs = set()
    for j, line in enumerate(reversed(lines)):
        for i, c in enumerate(line):
            if c == '#':
                elfs.add(complex(i, j))


neighbors = [1j, 1+1j, 1, 1-1j, -1j, -1-1j, -1, -1+1j]


def check(elf, adjacents, direction):
    n, ne, e, se, s, sw, w, nw = adjacents
    match direction:
        case 'north':
            if not (n in elfs or ne in elfs or nw in elfs):
                return 1j 
        case 'south':
            if not (s in elfs or se in elfs or sw in elfs):
                return -1j
        case 'west':
            if not (w in elfs or nw in elfs or sw in elfs):
                return -1 
        case 'east':
            if not (e in elfs or ne in elfs or se in elfs):
                return 1 
    return None


def visualize():
    for j in range(15, -5, -1):
        print(''.join('#' if complex(i, j) in elfs else '.' for i in range(-5, 15)))
    print()


didx = 0
directions = ['north', 'south', 'west', 'east']

round = 1
while True:
    moves = []
    for elf in elfs:
        adjacents = tuple(elf + neighbor for neighbor in neighbors)
        for adjacent in adjacents:
            if adjacent in elfs:
                break
        else:
            continue
        for i in range(4):
            mov = check(elf, adjacents, directions[(didx + i) % 4])
            if mov is not None:
                moves.append((elf + mov, elf))
                break
    
    count = Counter(target for target, _ in moves)
    moved = False
    for (target, elf) in moves:
        if count[target] == 1:
            elfs.remove(elf)
            elfs.add(target)    
            moved = True
    didx = (didx + 1) % 4

    if round == 10:
        min_x = min(elf.real for elf in elfs)
        max_x = max(elf.real for elf in elfs) + 1
        min_y = min(elf.imag for elf in elfs)
        max_y = max(elf.imag for elf in elfs) + 1

        area = (max_x - min_x) * (max_y - min_y)
        print(area - len(elfs))

    if not moved:
        print(round)
        break

    round += 1