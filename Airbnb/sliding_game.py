# 九宫格，一共8个方块，从1-8，一个方块空出来，然后打乱之后通过SLIDE还原，这个题要推广到N宫格，先实现这个游戏，然后对于一个任意的BOARD，要你把他解出来

#  A* algorithm

import heapq
import itertools
from copy import deepcopy

def heuristic(board, target = '123456780'):
    target = map(int, list(target))
    cur = map(int, list(board))
    return reduce(lambda acc, val: acc + (cur[val] - target[val])**2, range(len(target)))

def play(board, target = '123456780'): # board is list[list[char]]
    heap, visited, cur, m, n = [], set(), deepcopy(board), len(board), len(board[0])
    for i in len(cur):
        for j in len(cur[i]):
            if cur[i][j] == '0':
                key = ''.join(''.join(cur))
                heap = [(heuristic(key, target), i, j, key)]
                break
    while heap:
        _, x, y, key = heapq.heappop(heap)
        visited.add(key)
        if key == target:
            return True
        for d_x, d_y in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            n_x, n_y = x + d_x, y + d_y
            if n_x >= 0 and n_y >= 0 and n_x < m and n_y < n:
                new_pos = n_x * m + n_y
                old_pos = x * m + y
                new_board = list(key)
                new_board[new_pos], new_board[old_pos] = key[old_pos], key[new_pos]
                new_key = ''.join(new_board)
                if new_key not in visited:
                    heapq.heappush(heap, (heuristic(new_key, target), n_x, n_y, new_key))
    return False



