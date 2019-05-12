# `https://www.1point3acres.com/bbs/thread-452357-1-1.html`

# 概念题
# 1. 继承的作用是什么
# 2. 普通递归和尾递归区别
# 3. python generator的作用

# 代码题
# 1. 给一个字符串列表 返回最频繁的k个字符串
# 2. 给前序和中序遍历 还原二叉树 保证每个节点的值不重复
# 写完分析分析复杂度什么的

# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.

from collections import OrderedDict, defaultdict
from typing import List
import pysnooper


class Solution:
    @pysnooper.snoop()
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_to_freq = {}
        freq_to_word = defaultdict(lambda: set())
        for word in words:
            if word not in word_to_freq:
                word_to_freq[word] = 1
                freq_to_word[1].add(word)
            else:
                freq_to_word[word_to_freq[word]].remove(word)
                word_to_freq[word] += 1
                freq_to_word[word_to_freq[word]].add(word)
        res = []
        for freq in sorted(freq_to_word, reverse=True):
            if len(res) == k:
                break
            sorted_words = sorted(list(freq_to_word[freq]))
            res += sorted_words[:k - len(res)]
        return res


a = Solution()
res = a.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
print(res)
