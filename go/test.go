package main

import "fmt"

type human struct {
	name string
	age  uint
}

func main() {
	var person human
	fmt.Scan(&person.age, &person.name)
	fmt.Printf(person.name + " " + string(rune(person.age)))
}
