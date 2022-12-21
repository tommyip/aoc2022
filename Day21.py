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

g1 = g.copy()

while len(unvisited) > 0:
    for monkey in unvisited:
        left, op, right = g1[monkey]
        if left not in unvisited and right not in unvisited:
            a = g1[left]
            b = g1[right]
            match op:
                case '+':
                    g1[monkey] = a + b
                case '-':
                    g1[monkey] = a - b
                case '*':
                    g1[monkey] = a * b
                case '/':
                    g1[monkey] = int(a / b)
            unvisited.remove(monkey)
            break

print(g1['root'])
