from tqdm import tqdm
from llist import dllist

with open('inputs/day20.txt') as f:
    nums = list(map(int, f.read().strip().split('\n')))

n = len(nums)
nums = dllist(nums)
num_refs = list(nums.iternodes())


def cyclic_next(node):
    if node.next is not None:
        return node.next
    else:
        return nums.first


def cyclic_prev(node):
    if node.prev is not None:
        return node.prev
    else:
        return nums.last


for node in tqdm(num_refs):
    slot = node
    if node.value != 0:
        if node.value > 0:
            for i in range(node.value):
                slot = cyclic_next(slot)
                if slot == node:
                    slot = cyclic_next(slot)
        elif node.value < 0:
            for i in range((-node.value + 1)):
                slot = cyclic_prev(slot)
                if slot == node:
                    slot = cyclic_prev(slot)
        if slot != node:
            nums.remove(node)
            nums.insertafter(node, slot)

values = list(nums.itervalues())
zero_idx = values.index(0)

idx_1000 = (1000 + zero_idx) % n
idx_2000 = (2000 + zero_idx) % n
idx_3000 = (3000 + zero_idx) % n
print(values[idx_1000] + values[idx_2000] + values[idx_3000])
