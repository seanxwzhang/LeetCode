# leetcode 251（https://leetcode.com/problems/flatten-2d-vector）
# 实现二维数组的迭代器，加上remove操作。代码如下：

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.row = 0
        self.col = 0

    def next(self):
        """
        :rtype: int
        """
        tmp = self.vec2d[self.row][self.col]
        self.col += 1
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]): # move to next self.row until last self.row passed or valid
            self.row += 1
            self.col = 0
        if self.row >= len(self.vec2d): # if last self.row has passed, false
            return False
        return True

    def remove(self):
        """
        :rtype: None
        """
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]): # move to next self.row until last self.row passed or valid
             self.row += 1
             self.col = 0
        if self.row < len(self.vec2d) and self.col < len(self.vec2d[self.row]):
            tmp = self.vec2d[self.row][self.col]
            del self.vec2d[self.row][self.col]
            return tmp
        return None

vec2d = [[1,23,4,1,54,4],[],[3,3,2,1],[1],[3]]
s = Vector2D(vec2d)
while True:
    p = s.remove()
    if p:
        print(p)
    else:
        break
