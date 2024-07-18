package main

import "fmt"
func main(){
	var nums [4]int

	//length of arrays
	fmt.Println(len(nums))

	//adding elements 
	nums[0] = 1
	fmt.Println(nums)

	var strs[4]string
	fmt.Println(strs)

	var bools[4]bool
	fmt.Println(bools)

	// add values while declaring the array
	numbers := [3]int{1,2,3}
	fmt.Println(numbers)

	// creation of 2D array
	twoDnums := [2][2]int{{1,2},{4,5}}
	fmt.Println(twoDnums)
}