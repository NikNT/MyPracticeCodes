package main

import "fmt"
func main ()  {
	age := 10
	if age >= 18{
		fmt.Println("Person is an adult.")
	} else if age <= 10  {
		fmt.Println("Person is a child.")
	} else {
		fmt.Println("Person is a minor.")
	}

	var role = "admin"
	var hasPerm = false

	if role == "admin" && hasPerm {
		fmt.Println("Auth : Yes")
	}

	// variable can be declared inside 'if'
	if age := 15; age >= 18  {
		fmt.Println("Person is an adult.", age)
	} else if age >= 12 {
		fmt.Println("Person is a teengaer.", age)
	}

	// go does not have ternary operator
}