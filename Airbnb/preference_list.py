# 每个人都有一个preference的排序，在不违反每个人的preference的情况下得到总体的preference的排序 拓扑排序解决(https://instant.1point3acres.com/thread/207601)
import itertools
import collections

def preferenceList1(prefList): # topological sort 1
    pairs = []
    for lis in prefList:
        for left, right in zip(lis, lis[1:]):
            pairs += (left, right),
    allItems, res = set(itertools.chain(*pairs)), []
    while pairs:
        free = allItems - set(zip(*pairs)[1])
        if not free:
            None
        res += list(free)
        pairs = filter(free.isdisjoint, pairs)
        allItems -= free
    return res + list(allItems)


print(preferenceList1([[1, 2, 3, 4], ['a', 'b', 'c', 'd'], ['a', 1, 8], [2, 'b', 'e'], [3, 'c']]))