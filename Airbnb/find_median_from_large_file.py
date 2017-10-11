# -*- coding: UTF-8 -*-
# https://instant.1point3acres.com/thread/159344
# 二分查找
# 思路就是：先找在INT_MIN和INT_MAX的median（0？），然后读large file of integers，找出比这个数小的个数是否有一半，然后调整二分的边界

# assuming delimiter is ',', no new lines

def file_split(f, delim=',', bufsize=1024):
    prev = ''
    while True:
        s = f.read(bufsize)
        if not s:
            break
        split = s.split(delim)
        if len(split) > 1:
            yield prev + split[0]
            prev = split[-1]
            for x in split[1:-1]:
                yield x
        else:
            prev += s
    if prev:
        yield prev

def findMedian(file, min_num=-0xFFFFFFFF, max_num=0xFFFFFFFF):
    with open(file, 'r') as infile:
        while True:
            small_count, big_count, median = 0, 0, (float(min_num)/2 + float(max_num)/2)
            infile.seek(0)
            for num in file_split(infile):
                small_count += 1 if float(num) < median else 0
                big_count += 1 if float(num) > median else 0
            if small_count == big_count:
                break
            elif small_count < big_count:
                min_num = int(median) + 1
            else:
                max_num = int(median)
    return int(median)
            
print(findMedian('/Users/xiaowenzhang/Dropbox/projects/LeetCode/Airbnb/test.txt'))


            