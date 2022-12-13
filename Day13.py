from functools import cmp_to_key

with open('inputs/day13.txt') as f:
    pairs = f.read().strip().split('\n\n')
    pairs = [pair.split('\n') for pair in pairs]
    pairs = [(eval(pair[0]), eval(pair[1])) for pair in pairs]

def compare(l, r):
    match (isinstance(l, int), isinstance(r, int)):
        case (True, True):
            return l - r
        case (False, False):
            for i in range(min(len(l), len(r))):
                ans = compare(l[i], r[i])
                if ans != 0:
                    return ans
            return len(l) - len(r)
        case (True, False):
            return compare([l], r)
        case (False, True):
            return compare(l, [r])

part1 = 0
for i, (l, r) in enumerate(pairs):
    if compare(l, r) < 0:
        part1 += i + 1
print(part1)

packets = [value for pair in pairs for value in pair]
packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare))
part2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
print(part2)
