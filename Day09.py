from dataclasses import dataclass

with open('inputs/day09.txt') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]
    moves = [line[0] for line in lines for _ in range(int(line[1]))]

@dataclass
class Coord:
    x: str = 0
    y: str = 0

def sign(x):
    return x and (1, -1)[x < 0]

knots = [Coord() for _ in range(10)]
head = knots[0]
visited_2 = {(0, 0)}
visited_tail = {(0, 0)}
for move in moves:
    match move:
        case 'U':
            head.y += 1
        case 'R':
            head.x += 1
        case 'D':
            head.y -= 1
        case 'L':
            head.x -= 1
    for i in range(9):
        leader = knots[i]
        follower = knots[i+1]
        if follower.y == leader.y:
            if abs(leader.x - follower.x) > 1:
                follower.x += sign(leader.x - follower.x)
        elif follower.x == leader.x:
            if abs(leader.y - follower.y) > 1:
                follower.y += sign(leader.y - follower.y)
        else:
            if abs(leader.x - follower.x) > 1 or abs(leader.y - follower.y) > 1:
                follower.x += sign(leader.x - follower.x)
                follower.y += sign(leader.y - follower.y)
    visited_2.add((knots[1].x, knots[1].y))
    visited_tail.add((knots[9].x, knots[9].y))

print(len(visited_2))
print(len(visited_tail))
