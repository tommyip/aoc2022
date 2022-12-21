with open('inputs/day21.txt') as f:
    lines = f.read().strip().split('\n')
    g = {}
    unvisited = set()
    for line in lines:
        name, arg = line.split(': ')
        if arg.isdecimal():
            g[name] = int(arg)
        else:
            g[name] = tuple(arg.split(' '))
            unvisited.add(name)

g1 = {**g, 'humn': 'x'}
unvisited1 = unvisited.copy()

while len(unvisited) > 0:
    for monkey in unvisited:
        left, op, right = g[monkey]
        if left not in unvisited and right not in unvisited:
            a = g[left]
            b = g[right]
            match op:
                case '+':
                    g[monkey] = a + b
                case '-':
                    g[monkey] = a - b
                case '*':
                    g[monkey] = a * b
                case '/':
                    g[monkey] = int(a / b)
            unvisited.remove(monkey)
            break

print(g['root'])

while len(unvisited1) > 0:
    for monkey in unvisited1:
        left, op, right = g1[monkey]
        if left not in unvisited1 and right not in unvisited1:
            a = g1[left]
            b = g1[right]
            if isinstance(a, int) and isinstance(b, int):
                match op:
                    case '+':
                        g1[monkey] = a + b
                    case '-':
                        g1[monkey] = a - b
                    case '*':
                        g1[monkey] = a * b
                    case '/':
                        g1[monkey] = int(a / b)
            else:
                if monkey == 'root':
                    op = '='
                g1[monkey] = f'({a} {op} {b})'
            unvisited1.remove(monkey)
            break

# Plug equation to https://math.microsoft.com/en
print(g1['root'])
