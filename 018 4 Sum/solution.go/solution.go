// Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

// Note: The solution set must not contain duplicate quadruplets.

// For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

// A solution set is:
// [
//   [-1,  0, 0, 1],
//   [-2, -1, 1, 2],
//   [-2,  0, 0, 2]
// ]

// the idea is the same as 3 sum, and use a recursive approach to do KSum
package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int, target int) [][]int {
	res := [][]int{}
	for i := range nums {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		l, r := i+1, len(nums)-1
		for l < r {
			s := nums[i] + nums[l] + nums[r]
			if s < target {
				l++
			} else if s > target {
				r--
			} else {
				res = append(res, []int{nums[i], nums[l], nums[r]})
			L:
				for l < r {
					switch {
					case nums[l] == nums[l+1]:
						l++
					case nums[r] == nums[r-1]:
						r--
					default:
						break L
					}
				}
				l++
				r--
			}
		}
	}
	return res
}

func KSum(nums []int, target int, k int) [][]int {
	if k == 3 { //* base case
		return threeSum(nums, target)
	}
	res := [][]int{}
	for i := range nums {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		candidates := nums[i+1:]
		newTarget := target - nums[i]
		tmp := KSum(candidates, newTarget, k-1)
		if len(tmp) > 0 {
			for _, v := range tmp {
				res = append(res, append([]int{nums[i]}, v...))
			}
		}
	}
	return res
}

func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	return KSum(nums, target, 4)
}

func main() {
	sums := []int{-1, -5, -5, -3, 2, 5, 0, 4}
	res := fourSum(sums, -7)
	fmt.Println(res)
}
