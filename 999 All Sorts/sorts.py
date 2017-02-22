#!/usr/bin/env python
# my implementation of different sort algorithms

import time
import sys
from random import randint

# in-place
def bubble_sort(nums):
    while True:
        swapped = False
        for i, val in enumerate(nums):
            if i >= 1 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                swapped = True
        if not swapped:
            return nums

# more efficient by keeping a sorted sublist
def bubble_sort1(nums):
    for i in xrange(len(nums)):
        for j in xrange(len(nums) - 1, i, -1):
            if (nums[j] < nums[j - 1]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums;

# in-place
def selection_sort(nums):
    for partition in xrange(len(nums)):
        i, smallest, smallest_ind = partition, nums[partition], partition
        while (i < len(nums)):
            if nums[i] < smallest:
                smallest, smallest_ind = nums[i], i
            i += 1
        nums[smallest_ind], nums[partition] = nums[partition], nums[smallest_ind]
    return nums

# in-place
def insertion_sort(nums):
    for i in xrange(len(nums)):
        for j in xrange(i, 0, -1):
            if (nums[j] < nums[j - 1]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    if len(nums) == 2:
        return [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]
    left = merge_sort(nums[0:len(nums)/2])
    right = merge_sort(nums[len(nums)/2:])
    i, j, merge = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
    while i < len(left): merge.append(left[i]); i += 1
    while j < len(right): merge.append(right[j]); j += 1
    return merge

def findmedian(nums):
    sorted_list = sorted(enumerate([nums[0], nums[len(nums) - 1], nums[(len(nums) - 1)/2]]), key=lambda x:x[1])
    return sorted_list[1]

def partition(nums):
    pivot, l, r = nums[len(nums) - 1], 0, len(nums) - 2
    while l < r:
        while nums[l] <= pivot and l <= r:
            l += 1
        while nums[r] >= pivot and l <= r:
            r -= 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
    nums[l], nums[len(nums) - 1] = pivot, nums[l]
    return l


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    if len(nums) == 2:
        return [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]
    pivot = partition(nums)
    left = quick_sort(nums[0:pivot])
    right = quick_sort(nums[pivot:])
    left.extend(right)
    return left




def performance_test(sort_methods):
    N, l, r, testcase = 1000, 0, 100000, []
    for i in xrange(N):
        testcase.append(randint(l, r))
    for sort in sort_methods:
        starttime = time.time()
        sort(testcase)
        endtime = time.time()
        print(sort.__name__ + " takes " + str(endtime - starttime) + " seconds")

def validate(sort):
    N, l, r, testcase = 15, 0, 100, []
    for i in xrange(N):
        testcase.append(randint(l, r))
    # testcase = [66, 17, 7, 61, 5, 66, 67, 68, 58, 14, 62, 75, 73, 26, 48]
    print('sorting ' + str(testcase))
    for sorty in sort:
        print(sorty.__name__ + ": " + str(sorty(testcase[:])))


if __name__ == "__main__":
    sort_methods = [merge_sort, quick_sort, insertion_sort, selection_sort, bubble_sort1]
    validate(sort_methods)
    performance_test(sort_methods)