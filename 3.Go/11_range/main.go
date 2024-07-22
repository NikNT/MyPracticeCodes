package main

import "fmt"
func main(){
	nums := []int{6,7,8}

	for i:=0; i<len(nums); i++{
		fmt.Println(nums[i])
	}

	sum := 0
	for i, num := range nums {
		sum = sum + num
		fmt.Println("num", i, num)
	}
	fmt.Println("Sum", sum)

	m := map[string]string{
		"fname" : "John", 
		"lname" : "Doe",
	}

	for key, value := range m{
		fmt.Println(key, value)
	}

	for i, c := range "golang" {
		fmt.Println(i,c,string(c))
	}
}