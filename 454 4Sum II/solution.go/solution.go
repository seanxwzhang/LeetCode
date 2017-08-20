// Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

// To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

// Example:

// Input:
// A = [ 1, 2]
// B = [-2,-1]
// C = [-1, 2]
// D = [ 0, 2]

// Output:
// 2

// Explanation:
// The two tuples are:
// 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
// 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
package main

import (
	"fmt"
)

func findSums(A []int, B []int) []int {
	sums := map[int]bool{}
	for _, vA := range A {
		for _, vB := range B {
			sums[vA+vB] = true
		}
	}
	res := make([]int, 0, len(sums))
	for k := range sums {
		res = append(res, k)
	}
	return res
}

func fourSumCount(A []int, B []int, C []int, D []int) int {
	sumAB := findSums(A, B)
	sumCD := findSums(C, D)
	for
}

func main() {
	sums := []int{-1, -5, -5, -3, 2, 5, 0, 4}
	res := fourSum(sums, -7)
	fmt.Println(res)
}
