from collections import deque

class Solution:
    def find_treasure(self, world):
        for i, row in enumerate(world):
            for j, char in enumerate(row):
                if char == 'S':
                    return (i, j)

    def initialize(self, world):
        melting_ices = set()
        m, n = len(world), len(world[0])
        # add surrounding ice blocks
        melting_ices |= set([(0, j) for j in range(n)])
        melting_ices |= set([(m-1, j) for j in range(n)])
        for i in range(1, len(world) - 1):
            melting_ices.add((i, 0))
            melting_ices.add((i, n - 1))
            # add initial non-ice places
            for j in range(n):
                if world[i][j] != 'I':
                    melting_ices.add((i, j))
        return melting_ices

    def melting_ice(self, world):
        treasure = self.find_treasure(world)
        accessible = []
        melting_set = self.initialize(world)
        time = 0
        while True:
            time += 1
            for 


