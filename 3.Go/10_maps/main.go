package main

import (
	"fmt"
	"maps"
)
func main(){
	// creating maps
	m := make(map[string]string)

	// setting elements
	m["name"] = "golang"
	m["area"] = "backend"

	// get an element
	fmt.Println(m["name"], m["area"], m["key"])

	// If key does not exist in the Map, then it returns zero value

	m2 := make(map[string]int)
	m2["age"] = 30
	m2["price"] = 2
	fmt.Println(m2["age"], m2["phone"])

	// length of map
	fmt.Println(len(m), len(m2))

	//delete a key-value pair
	delete(m2, "price")

	fmt.Println(m2)

	//clear a map
	clear(m2)
	fmt.Println(m2)

	m3 := map[string]int{
		"price" : 20,
		"phones" : 3,
	}

	fmt.Println(m3)

	// check element in map
	v, ok := m3["price"]
	fmt.Println(v)
	if ok{
		fmt.Println("OK!")
	} else {
		fmt.Println("Err!")
	}

	// check if maps are equal
	m4 := map[string]int{
		"price" : 20,
		"phones" : 30,
	}
	fmt.Println(maps.Equal(m3, m4))
}