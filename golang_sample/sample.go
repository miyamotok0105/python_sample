package main
import "fmt"
import("strconv")

//基礎
//https://qiita.com/kazusa-qooq/items/40f9ea3e72406d845b10
//===========================
//型
// int：初期値 0
// float32: 初期値 0
// bool: 初期値 false
// string: 初期値 ""
// complex64: 初期値 (0+0i)

//===========================
//goにはclassが存在しない。typeの構造体を使用する。

// class Taiyaki
//     def atama
//         puts "たい焼きの頭の方にはあんこがいっぱい入っている"
//     end

//     def shippo
//         puts "たい焼きの尻尾にはあんこがほとんど入っていない"
//         puts "しかしカリカリしていて美味しい"
//     end
// end

type Taiyaki struct{}
//(t Taiyaki)の部分をメソッドレシーバという。
func (t Taiyaki) Atama() {
    fmt.Println("たい焼きの頭の方にはあんこがいっぱい入っている")
}

func (t Taiyaki) Shippo() {
    fmt.Println("たい焼きの尻尾にはあんこがほとんど入っていない")
    fmt.Println("しかしカリカリしていて美味しい")
}
//===========================


func main(){
    fmt.Printf("Hello, world\n")

    //配列
    ArrayInt := []int{2, 3, 5, 7, 11, 13}
    ArrayStr := []string{"2", "3", "5", "7", "11", "13"}

    fmt.Printf("===========")
    fmt.Printf("配列のfor文")
    for i := 0; i < len(ArrayInt); i++ {
      fmt.Printf("array[%d] == %d\n", i, ArrayInt[i])
    }
    for i := 0; i < len(ArrayStr); i++ {
      fmt.Printf("array[%d] == %d\n", i, ArrayStr[i])
    }

    fmt.Printf("===========")
    fmt.Printf("部分配列")
    fmt.Println(ArrayInt[1:3])
    fmt.Println(ArrayInt[:3])

    fmt.Printf("===========")
    fmt.Printf("Map")

    var m = map[string]int{
        "Bell Labs": 1,
        "Google": 2 ,
    }
    m["Google"] = 1
    fmt.Println(m)

    fmt.Printf("===========")
    fmt.Printf("変数宣言")
    var x, y int
    var x2, y2, z2 = 0, 0.1, "str"
    fmt.Println(x, y)
    fmt.Println(x2, y2, z2)

    fmt.Printf("===========")
    fmt.Printf("関数")
    refFunc1 := Func1()
    fmt.Printf(refFunc1)

    fmt.Printf("===========")
    fmt.Printf("定数\n")
    const (
        name1 = 1
        name2 = 2
    )
    fmt.Println(name2)

    fmt.Printf("===========")
    fmt.Printf("ループ\n")
    for i := 0; i < 10; i++ {
        fmt.Printf(" i:"+strconv.Itoa(i))
    }
    fmt.Printf("\n")

    fmt.Printf("===========")
    fmt.Printf("\n")
    var i2 int = 1
    for i2 < 10 {
        fmt.Printf(" i2:"+strconv.Itoa(i2))
        i2 = i2 + 1
        if i2 == 6 {
            break
        }
    }
    fmt.Printf("\n")

    fmt.Printf("===========")
    fmt.Printf("type\n")

    taiyakikun1 := new(Taiyaki)
    taiyakikun1.Atama()
    fmt.Printf("\n")
}


func Func1() string {
  x := "a"
  return x
}

