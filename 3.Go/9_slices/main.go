package main

import (
	"fmt"
	"slices"
)
func main(){
	// uninitialized slice is nil
	var nums []int;
	fmt.Println(nums, len(nums))

	var nums2 = make([]int, 0, 5)
	fmt.Println(nums2)
	
	// cap is the max number of elements that can fit
	fmt.Println(cap(nums2)) 

	nums2 = append(nums2, 1)
	nums2 = append(nums2, 2)
	nums2 = append(nums2, 3)

	fmt.Println(nums2, cap(nums2), len(nums2)) 

	nums3 := []int{}
	nums3 = append(nums3, 1)
	fmt.Println(nums3)
	
	// copy function 
	var nums4 = make([]int, 0, 5)
	nums4 = append(nums4, 2)

	var nums4_copy = make([]int, len(nums4))
	copy(nums4_copy, nums4)
	fmt.Println(nums4, nums4_copy)

	//slice operator
	var nums5 = []int{1,2,3}
	fmt.Println(nums5[0:1])

	//slice package
	var nums6 = []int{1,2}
	var nums7 = []int{1,2}

	fmt.Println(slices.Equal(nums6, nums7))

	//2d slices
	var nums8 = [][]int{{1,2,3}, {4,5,6}}
	fmt.Println(nums8)

}