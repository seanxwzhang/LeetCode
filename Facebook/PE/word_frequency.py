# 1. 给你一本书(input)，统计里面词频最高的10个单词
# 先是说考虑input是一个大string的情况，用hashmap+maxheap直接秒就行了，注意一些细节处理就好，我写完被挑出一些小毛病，改完小哥很满意然后上follow up: input是一个文件？改下代码的input处理就好了，按行读入按单词存入hashmap。写完继续follow up：如果input文件很大，hashmap爆了内存怎么办？只考虑ASCII。然后开始估算大概要用多少内存，算下来几M到几十M不等的内存占用，然后pass
import collections
import heapq

def word_frequency(input, n):
    """
    input: list[str]
    n: int
    """
    table, heap, res = collections.defaultdict(0), [], []
    for word in input:
        input[word] += 1
    heap = [(-table[word], word) for word in table]
    heapq.heapify(heap)
    for _ in xrange(n):
        res.append(heapq.heappop())
    return res

def file_word_frequence(file, n):
    table, heap, res = collections.defaultdict(0), [], []
    with open(file, 'r') as input:
        for word in input:
            input[word] += 1
        heap = [(-table[word], word) for word in table]
        heapq.heapify(heap)
    for _ in xrange(n):
        res.append(heapq.heappop())
    return res