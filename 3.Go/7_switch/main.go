package main

import (
	"fmt"
	"time"
)
func main(){
	// simple switch 
	i := 3
	switch i{
	case 1:
		fmt.Println("One")
	case 2:
		fmt.Println("Two")
	case 3:
		fmt.Println("Three")
	default:
		fmt.Println("None")
	}

	// multiple condition switch
	switch time.Now().Weekday(){
	case time.Saturday, time.Sunday:
		fmt.Println("Weekend")
	default:
		fmt.Println("Weekday")
	}

	//type switch
	whoAmI := func (i interface{})  {
		switch i.(type){
		case int:
			fmt.Println("It's an integer")
		case string:
			fmt.Println("It's a string")
		case bool:
			fmt.Println("It's a boolean")
		default:
			fmt.Println("Other")
		} 
	}

	whoAmI(true)
}