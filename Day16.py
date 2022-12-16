import re
from itertools import combinations
from tqdm import tqdm

g = {}
rates = {}

with open('inputs/day16.txt') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        tokens = line.split(' ')
        cur = tokens[1]
        g[cur] = tuple(map(lambda x: x.rstrip(','), tokens[9:]))
        rates[cur] = int(tokens[4][5:-1])

# print(g)

def dfs(source):
    distance = {}
    def aux(node, travelled = 0):
        neighbors = g[node]
        for neighbor in neighbors:
            if neighbor != source:
                if neighbor in distance:
                    if travelled + 1 < distance[neighbor]:
                        distance[neighbor] = travelled + 1
                        aux(neighbor, travelled + 1)
                else:
                    distance[neighbor] = travelled + 1
                    aux(neighbor, travelled + 1)
    aux(source)
    return distance

paths = {}
for source in g:
    paths[source] = dfs(source)

def visit(node, unvisited, remaining, pressure):
    if remaining < 0:
        return None
    if len(unvisited) == 0:
        return pressure
    max_pressure = pressure
    for target in unvisited:
        distance = paths[node][target]
        time = distance + 1
        new_pressure = visit(target, unvisited - {target}, remaining - time, pressure + rates[target] * (remaining - time))
        if new_pressure is not None and new_pressure > max_pressure:
            max_pressure = new_pressure
    return max_pressure

valves = {node for (node, rate) in rates.items() if rate > 0 and node != 'AA'}
print(visit('AA', valves, 30, 0))

max_pressure = 0
# Only need to test half as the remaining are just inverse
for i in tqdm(range(1, len(valves)//2 + 1)):
    for me in tqdm(combinations(valves, i)):
        me = set(me)
        elephant = valves - me
        me_pressure = visit('AA', me, 26, 0)
        elephant_pressure = visit('AA', elephant, 26, 0)
        max_pressure = max(max_pressure, me_pressure + elephant_pressure)
print(max_pressure)
