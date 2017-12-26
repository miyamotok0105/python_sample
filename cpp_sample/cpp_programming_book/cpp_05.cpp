#include <iostream>
//g++  -I/usr/local/include cpp_05.cpp -o cpp_05

int main(void)
{
    std::cout << "数字を入力してください。" << std::endl;
    std::cout << "0入力で終了します。" << std::endl;
    while(1) {
        int a;
        static int n = 0;
        std::cin >> a;
        if (a == 0)
            break;
        n++;
        std::cout << "第" << n << "回の入力は" << a << "です。" << std::endl;
        
    }
    //スコープ外でのエラーの例
    // cout << "n=" << n; //エラー！
    // cout << "a=" << a; //エラー！　
    return 0;
}

