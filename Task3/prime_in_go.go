package main

import (
	"fmt"
	"math"
)

func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var num int
	fmt.Print("Enter n: ")
	fmt.Scanln(&num)
	fmt.Println("Prime Numbers are:")
	for i := 2; i < num; i++ {
		if isPrime(i) {
			fmt.Printf("%d ", i)
		}
	}
}
