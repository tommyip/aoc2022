from tqdm import tqdm
from llist import dllist

with open('inputs/day20.txt') as f:
    nums = list(map(int, f.read().strip().split('\n')))


def solve(nums, key, n_mix):
    n = len(nums)
    for i in range(n):
        nums[i] *= key
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

    for _ in tqdm(range(n_mix)):
        for i in range(n):
            node = num_refs[i]
            value = node.value
            if value != 0:
                slot = cyclic_next(node) if value > 0 else cyclic_prev(node)
                nums.remove(node)
                if value > 0:
                    m = (value - 1) % (n - 1)
                    for _ in range(m):
                        slot = cyclic_next(slot)
                elif value < 0:
                    m = -value % (n - 1)
                    for _ in range(m):
                        slot = cyclic_prev(slot)
                num_refs[i] = nums.insertafter(value, slot)

    values = list(nums.itervalues())
    zero_idx = values.index(0)

    idx_1000 = (1000 + zero_idx) % n
    idx_2000 = (2000 + zero_idx) % n
    idx_3000 = (3000 + zero_idx) % n
    return values[idx_1000] + values[idx_2000] + values[idx_3000]


print(solve(nums, 1, 1))
print(solve(nums, 811589153, 10))
