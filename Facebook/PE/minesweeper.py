# Given a height and a width and number of mines, return a minesweeper field with mines in random positions input: 2, 3, 3 return: ------------- - - - X - ------------- - X - X - - ------------- 

# 链接: https://instant.1point3acres.com/thread/183712/post/2008134
# 来源: 一亩三分地
import random

def minesweeper(height, width, n):
    if n < height * width / 2:
        matrix = [['-'] * width for _ in xrange(height)]
        for num in random.sample(xrange(0, height * width), n):
            matrix[num/width][num%width] = 'X'
    else:
        matrix = [['X'] * width for _ in xrange(height)]
        if n < height * width:
            m = height * width - n
            for num in random.sample(xrange(0, height * width), m):
                matrix[num/width][num%width] = '-'
    print(''.join([char for row in matrix for char in row + ['\n']]))

minesweeper(5,6,20)