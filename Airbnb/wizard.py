# wizards

# There are 10 wizards, 0-9, you are given a list that each entry is a list of wizards known by wizard. Define the cost between wizards and wizard as square of different of i and j. To find the min cost between 0 and 9. +

# 说白了，就是带权重的最短距离，最优解是Dijkstra algorithm。似乎面试官说，只要普通的BFS能得到解也是可以的，Dijkstra我最近正好写过，所以也写出来了。（https://instant.1point3acres.com/thread/218032）
import heapq

def min_distance(wizards, start = 0, end = 9):
    table = {i: set(entry) for i, entry in enumerate(wizards)}
    costtable = {i: float('inf') for i in xrange(len(wizards))}
    costtable[start] = 0
    cost = [(wizard**2, start, wizard) for wizard in table[start]]
    heapq.heapify(cost)
    while costtable[end] == float('inf'):
        cur_cost, from_wizard, cur_wizard = heapq.heappop(cost)
        costtable[cur_wizard] = costtable[from_wizard] + cur_cost
        for reachable in table[cur_wizard]:
            if costtable[reachable] == float('inf'):
                heapq.heappush(cost, ((reachable - cur_wizard)**2, cur_wizard, reachable))
    return costtable[end]

wizards = [
    [1, 3, 7, 9],
    [0, 5],
    [1],
    [0, 2, 5, 4, 6],
    [3],
    [1, 3, 6],
    [3, 5, 7],
    [0, 6, 9],
    [],
    [0, 7]
]

print(min_distance(wizards))