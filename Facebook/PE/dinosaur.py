# 1、恐龙题
# 给两个cvs files里面给了一些数据，格式大概是这样的
# file1
# name,leg_length,diet
# file2:
# name,stride_length,stance
# 两个files里的恐龙的名字是对应的，但是不顺序
# 要求是根据给定的一个公式（输入是leg_length和stride_length）计算出速度，从大到小输出直立行走的恐龙名字
import collections
import os

def printDinosaur(speedOf, file1, file2):
	dTable = collections.defaultdict(list)
	with open(file1, 'r') as csv1, open(file2, 'r') as csv2:
		for line in csv1:
			try:
				dinosaur, leg_length, diet = line.split(',')
			except TypeError as err:
				print('Input error: {0}'.format(err))
			else:
				dTable[dinosaur].append(int(leg_length))
		for line in csv2:
			try:
				dinosaur, stride_length, stance = line.split(',')
			except TypeError as err:
				print('Input error: {0}'.format(err))
			else:
				dTable[dinosaur].append(int(stride_length))
		col = [(name, dTable[name][0], dTable[name][1]) for name in dTable]
		col.sort(cmp=lambda a,b: speedOf(a[1], a[2]) - speedOf(b[1], b[2]), reverse=True)
	print(col)
	return [elt[0] for elt in col]

def speedOf(leg, stride):
	return leg * stride

print(printDinosaur(speedOf, 'Facebook/PE/dinosaur1.csv', 'Facebook/PE/dinosaur2.csv'))