package main

import "fmt"

//戻り値となる変数に名前をつけることができる。( named return value )
//xとyは関数内で名前付きの戻り値として使用できる。
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

func main() {
    fmt.Println(split(17))
}

