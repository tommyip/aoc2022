from collections import namedtuple
import operator
from functools import reduce

Monkey = namedtuple('Monkey', ['items', 'op', 'op_value', 'divisor', 'throw_true', 'throw_false'])

with open('inputs/day11.txt') as f:
    blocks = f.read().strip().split('\n\n')
    monkeys = []
    for block in blocks:
        lines = block.split('\n')
        items_list = lines[1].split(': ')
        starting_items = []
        if len(items_list) == 2:
            starting_items = [int(item) for item in items_list[1].split(', ')]
        [op, value] = lines[2].split(' ')[-2:]
        op = operator.add if op == '+' else operator.mul
        value = None if value == 'old' else int(value)
        divisor = int(lines[3].split()[-1])
        throw_true = int(lines[4].split()[-1])
        throw_false = int(lines[5].split()[-1])
        monkeys.append(Monkey(starting_items, op, value, divisor, throw_true, throw_false))

mod = reduce(operator.mul, (monkey.divisor for monkey in monkeys))
inspections = [0] * len(monkeys)

# # Part 1
# for round in range(20):
#     for i, monkey in enumerate(monkeys):
#         for item in monkey.items:
#             item = monkey.op(item, monkey.op_value or item)
#             item //= 3
#             monkeys[monkey.throw_true if item % monkey.divisor == 0 else monkey.throw_false].items.append(item)
#         inspections[i] += len(monkey.items)
#         monkey.items.clear()

for round in range(10000):
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            item = monkey.op(item, monkey.op_value or item)
            monkeys[monkey.throw_true if item % monkey.divisor == 0 else monkey.throw_false].items.append(item % mod)
        inspections[i] += len(monkey.items)
        monkey.items.clear()

inspections.sort()
print(inspections[-1] * inspections[-2])
