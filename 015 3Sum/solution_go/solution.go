package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	res := [][]int{}
	sort.Ints(nums)
	for i := range nums {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		l, r := i+1, len(nums)-1
		for l < r {
			s := nums[i] + nums[l] + nums[r]
			if s < 0 {
				l++
			} else if s > 0 {
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

func main() {
	sums := []int{-1, 0, 1, 2, -1, -4}
	res := threeSum(sums)
	fmt.Println(res)
}
