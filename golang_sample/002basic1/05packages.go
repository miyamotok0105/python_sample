package main

import "fmt"

//関数の引数が両方intなので、省略できる。
func add(x, y int) int {
    return x + y
}

func main() {
    fmt.Println(add(42, 13))
}

