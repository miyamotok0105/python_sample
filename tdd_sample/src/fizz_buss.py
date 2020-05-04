
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
仕様

入力した数字を返す
3の倍数 -> Fizz!
5の倍数 -> Buzz!
15の倍数 -> FizzBuzz!
"""
class FizzBuzz():
    def execute(self, num):
        if num % 15 == 0:
            return "FizzBuzz"
        if num % 3 == 0:
            return "Fizz"
        if num % 5 == 0:
            return "Buzz"

        return str(num)

if __name__ == '__main__':
    fb = FizzBuzz()
    fb.execute(1)
