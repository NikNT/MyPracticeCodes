package main

import "fmt"

func sum(nums ...int) int{
	total := 0
	for _,num:= range nums{
		total = total + num
	}
	return total
}


func main(){
	nums := []int{3,4,5,6}
	
	// Pass n number of parameters
	res := sum(nums...)
	fmt.Println(res)
}