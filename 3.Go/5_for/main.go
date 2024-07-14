package main

import "fmt"

// 'for' is the only construct in go for looping
func main(){

 // while loop
 i := 1
 for i <= 3{
	fmt.Println(i)
	i = i+1
 }

 // infinite loop
//  for {
// 	println("infinite")
//  }

 // for loop
 for i := 0; i<3; i++ {
	 // break
	 
	 if i == 2{
		 continue
		}
	println(i)
 } 

 for i := range 10 {
	fmt.Println(i)
 }

}
