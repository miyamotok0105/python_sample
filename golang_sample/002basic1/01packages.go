package main

//math/randパッケージもインポート
import (
    "fmt"
    "math/rand"
)

//rand.Intnを使用。
func main() {
    fmt.Println("My favorite number is", rand.Intn(10))
}

