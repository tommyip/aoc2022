with open('inputs/day12.txt') as f:
    lines = f.read().strip().split()
    m = []
    start = None
    end = None
    for j, line in enumerate(lines):
        row = []
        for i, c in enumerate(line):
            if c == 'S':
                start = (i, j)
                row.append(0)
            elif c == 'E':
                end = (i, j)
                row.append(25)
            else:
                row.append(ord(c) - ord('a'))
        m.append(row)

w, h = len(m[0]), len(m)

def steps(i, j):
    dp = [[None] * w for _ in range(h)]
    dp[j][i] = 0

    stack = [(i, j)]
    while len(stack) > 0:
        i, j = stack.pop()
        height = m[j][i]
        steps = dp[j][i]
        for di, dj in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < w and 0 <= nj < h:
                n_height = m[nj][ni]
                if n_height <= height + 1:
                    if dp[nj][ni] is None or dp[nj][ni] > steps + 1:
                        dp[nj][ni] = steps + 1
                        stack.append((ni, nj))

    return dp

dp = steps(*start)
part1 = dp[end[1]][end[0]]
print(part1)

part2 = part1
for j in range(h):
    for i in range(w):
        if m[j][i] == 0:
            step = steps(i, j)[end[1]][end[0]]
            if step is not None:
                part2 = min(part2, step)

print(part2)
