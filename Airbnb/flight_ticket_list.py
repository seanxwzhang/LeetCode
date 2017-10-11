# 每一项包括departure, arrival, cost，然后给一个整数k, 表示最多允许k次中转。给定起始地点A，到达地点B, 要求输出从A到B的最小花费，最多k次中转。BFS一层一层扫。
import collections

def min_cost(flights, start, end, k):
    table = collections.defaultdict(collections.defaultdict(float('inf')))
    for tour, cost in flights:
        st, ed = tour.split('->')
        table[st][ed] = cost
    if start not in table:
        return None
    queue = [place for place in table[start]]
    visited = set(queue)
    for _ in xrange(k):
        new_queue = []
        while queue:
            cur = queue.pop(0)
            for dest in table[cur]:
                table[start][dest] = min(table[start][dest], table[start][cur] + table[cur][dest])
                if dest not in visited:
                    new_queue += dest,
                    visited.add(dest)
        queue = new_queue
    return table[start][end]
