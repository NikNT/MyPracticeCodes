package main

import "fmt"

func add(a, b int) int {
	return a + b
}

func getLanguages() (string, string, string, bool) {
	return "golang", "javascript", "c", true
}

func process(fn func(a int) int) {
	result := fn(1)
	fmt.Println(result)
}

func pro() func(a int) int {
	return func(a int) int {
		return 4
	}
}

func main() {
	x := add(1, 2)
	fmt.Println(x)

	lang1, lang2, lang3, _ := getLanguages()
	fmt.Println(lang1, lang2, lang3)

	fn := func(a int) int {
		return a
	}

	ab := pro()
	process(ab)

	fmt.Println(fn(1))
}
