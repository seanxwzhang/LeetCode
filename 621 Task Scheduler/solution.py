# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

# looks like a greedy approach would work
import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        task_table = collections.defaultdict(lambda: 0)
        for task in tasks:
            task_table[task] += 1
        last_task, index = {task: None for task in task_table}, 0
        while task_table:
            to_do = None
            for task in last_task:
                if last_task[task] == None or index - last_task[task] > n:
                    to_do = task
                    break
            if to_do:
                task_table[to_do] -= 1
                last_task[to_do] = index
                if task_table[to_do] == 0:
                    del task_table[to_do]
                    del last_task[to_do]
            index += 1
        return index

s = Solution()
print(s.leastInterval(["A","B","C","A","B"], 2))