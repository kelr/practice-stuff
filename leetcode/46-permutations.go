package main

import "fmt"

// Given a collection of distinct integers, return all possible permutations
func permute(nums []int) [][]int {
	var result [][]int
	helper(nums, 0, &result)
	return result
}

func helper(nums []int, startIndex int, result *[][]int) {
	if startIndex == len(nums) - 1 {
		var tmp = make([]int, len(nums))
		copy(tmp, nums)
		*result = append(*result, tmp)
	}
	// Swap each subsequent element in num starting from startIndex
	for i := startIndex; i < len(nums); i++ {
		// Don't swap the same element with itself
		if i == startIndex {
			helper(nums, startIndex+1, result)
			continue
		}
		swap(&nums, startIndex, i)
		helper(nums, startIndex+1, result)
		swap(&nums, startIndex, i)
	}
}

// Swap two elements in a slice
func swap(arr *[]int, index1 int, index2 int) {
	temp := (*arr)[index1]
	(*arr)[index1] = (*arr)[index2]
	(*arr)[index2] = temp
}

func main() {
	fmt.Println(permute([]int{1,2,3}))
}
