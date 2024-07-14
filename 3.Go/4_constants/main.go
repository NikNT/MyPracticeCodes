package main

import "fmt"

const age = 30
var name = "var"

func main(){
	const name string = "golang"
	const age = 28
	fmt.Println(name,age)

	//multiple constants 
	const(
		port = 5000
		host = "localhost"
	)

	fmt.Println(port, host)
}