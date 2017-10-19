#include <stdio.h>
//g++  -I/usr/local/include cpp_04.cpp -o cpp_04
//オーバーロード

void print()
{
    printf("引数はありません\n");
    return;
}

void print(int x)
{
    printf("int型の引数%dです。\n", x);
    return;
}

void print(int a, char *b)
{
    printf("引数は%dと「%s」です。\n", a, b);
    return ;
}

int main(void)
{
    int a = 10;
    char *str = "粂井康孝";

    print();
    print(a);
    print(a, str);
    return 0;
}
