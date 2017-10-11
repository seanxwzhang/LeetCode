#!/usr/bin/env python
import collections

def generate_status(all_status, matrix):
    if len(all_status) == 1:
        return all_status[0]

    next_all_status = []
    for i in xrange(len(all_status) - 1):
        cur_status = set()
        for first in all_status[i]:
            for second in all_status[i + 1]:
                cur_status |= set(list(matrix[first][second]))
        next_all_status.append(cur_status)

    return generate_status(next_all_status, matrix)


def is_legal_status(nodes, status, matrix):
    all_status = [set(node) for node in nodes]
    return status in generate_status(all_status, matrix)

class Solution(object):
    def __init__(self, matrix, target):
        self.memo = {}
        self.matrix = matrix
        self.target = target

    def get_values(self, nodes): # BFS
        """
        nodes: list[set('a')]
        """
        if len(nodes) == 1:
            return nodes[0]
        next_nodes = []
        for left, right in zip(nodes, nodes[1:]):
            cur_node = set()
            for l in left:
                for r in right:
                    cur_node |= set(matrix[l][r])
            next_nodes.append(cur_node)
        return self.get_values(next_nodes)

    def get_value_2(self, nodes): #DFS
        """
        nodes: str
        """
        if len(nodes) == 1:
            return nodes[0] in self.target
        if nodes in self.memo:
            return self.memo[nodes]
        trials = [matrix[l][r] for l, r in zip(nodes, nodes[1:])]
        return self.dfs(trials, '')
        
    def dfs(self, nodes, accum):
        flag = (len(nodes) == 1)
        n = len(nodes[0])
        for i in xrange(n):
            new_nodes = accum + nodes[0][i]
            if flag:
                if self.get_value_2(new_nodes):
                    return True
            else:
                if self.dfs(nodes[1:], new_nodes):
                    return True
        return False


            
                
            





nodes = "ABCD"
matrix = collections.defaultdict(lambda: collections.defaultdict(list))
matrix['A']['A'] = ['B']
matrix['A']['B'] = ['A', 'C']
matrix['A']['C'] = ['D']
matrix['A']['D'] = ['A']
matrix['B']['A'] = ['D']
matrix['B']['B'] = ['B', 'C']
matrix['B']['C'] = ['A']
matrix['C']['D'] = ['B']
print is_legal_status(nodes, 'D', matrix)
s = Solution(matrix, ['D'])
print s.get_value_2(nodes)