package main

import "fmt"

//複数の戻り値を返せる
func swap(x, y string) (string, string) {
    return y, x
}

//:=で戻り値を受け取れる
func main() {
    a, b := swap("hello", "world")
    fmt.Println(a, b)
}
