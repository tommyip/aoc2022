from tqdm import tqdm

class Rock:
    def __init__(self, parts, pos):
        self.parts = parts
        self.move(pos)

    def move(self, offset):
        for i in range(len(self.parts)):
            self.parts[i] += offset


with open('inputs/day17.txt') as f:
    jet = [1 if c == '>' else -1 for c in f.read().strip()]


rock0 = [0+0j, 1+0j, 2+0j, 3+0j]
rock1 = [1+0j, 0+1j, 1+1j, 2+1j, 1+2j]
rock2 = [0+0j, 1+0j, 2+0j, 2+1j, 2+2j]
rock3 = [0+0j, 0+1j, 0+2j, 0+3j]
rock4 = [0+0j, 1+0j, 0+1j, 1+1j]
rocks = [rock0, rock1, rock2, rock3, rock4]

m = set()
jet_i = 0
rock_i = 0
level = 0

def collide(rock):
    for part in rock.parts:
        if part.imag == -1:  # on the floor
            return True
        if part in m:  # on a rock
            return True
        if part.real == -1 or part.real == 7: # walls
            return True
    return False


def fall(rock):
    global jet_i
    while True:
        rock.move(jet[jet_i])
        if collide(rock):
            rock.move(-jet[jet_i])
        jet_i = (jet_i + 1) % len(jet)
        rock.move(-1j)
        if collide(rock):
            rock.move(1j)
            break

def visualize(levels):
    for j in reversed(levels):
        print(''.join('#' if complex(i, j) in m else '.' for i in range(0, 7)))


for i in tqdm(range(1000)):
    rock = Rock(list(rocks[rock_i]), complex(2, level + 3))
    fall(rock)
    m.update(set(rock.parts))
    level = max(level, max(part.imag for part in rock.parts) + 1)
    rock_i = (rock_i + 1) % len(rocks)
    if i == 2021:
        print(int(level))

visualize(range(1000))

print(int(level))
