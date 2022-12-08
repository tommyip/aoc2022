with open('inputs/day08.txt') as f:
    m = [[int(height) for height in line] for line in f.read().strip().split('\n')]
    w, h = len(m[0]), len(m)

def part1(m):
    visible = set()
    for col in range(w):
        height_top = -1
        height_bottom = -1
        for row in range(h):
            if m[row][col] > height_top:
                visible.add((col, row))
                height_top = m[row][col]
            row_bottom = h - row - 1
            if m[row_bottom][col] > height_bottom:
                visible.add((col, row_bottom))
                height_bottom = m[row_bottom][col]
    for row in range(h):
        height_left = -1
        height_right = -1
        for col in range(w):
            if m[row][col] > height_left:
                visible.add((col, row))
                height_left = m[row][col]
            col_right = w - col - 1
            if m[row][col_right] > height_right:
                visible.add((col_right, row))
                height_right = m[row][col_right]
    return len(visible)

def part2(m):
    def heights(direction, row, col):
        i, j = col, row
        while 0 <= j < h and 0 <= i < w:
            if (j, i) != (row, col):
                yield m[j][i]
            if direction == 'up':
                j -= 1
            elif direction == 'right':
                i += 1
            elif direction == 'bottom':
                j += 1
            else:
                i -= 1

    def score(row, col):
        this = m[row][col]
        ans = 1
        for direction in ['up', 'left', 'bottom', 'right']:
            runningAns = 0

            for h in heights(direction, row, col):
                runningAns += 1
                if h >= this:
                    break
            ans *= runningAns
        return ans

    return max(score(j, i) for j in range(h) for i in range(w))

print(part1(m))
print(part2(m))
