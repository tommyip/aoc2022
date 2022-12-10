with open('inputs/day10.txt') as f:
    lines = f.read().strip().split('\n')

def commands(lines):
    for line in lines:
        match line.split():
            case ['noop']:
                yield None
            case ['addx', val]:
                yield None
                yield int(val)

reg_x = 1
part1 = 0
for i, cmd in enumerate(commands(lines)):
    cycle = i + 1
    if (cycle + 20) % 40 == 0:
        part1 += (cycle * reg_x)

    if cmd is not None:
        reg_x += cmd

print(part1)

reg_x = 1
crt = ['.'] * 40
for i, cmd in enumerate(commands(lines)):
    pixel_x = i % 40
    if reg_x - 1 <= pixel_x <= reg_x + 1:
        crt[pixel_x] = '#'
    if pixel_x == 39:
        print(''.join(crt))
        crt = ['.'] * 40
    if cmd is not None:
        reg_x += cmd
