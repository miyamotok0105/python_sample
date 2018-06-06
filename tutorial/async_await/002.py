import asyncio
#コルーチン1個
def fizzbuzz(i):
    if i == 15:
        return 'FizzBuzz'
    if i % 5 == 0:
        return 'Buzz'
    if i % 3 == 0:
        return 'Fizz'
    return str(i)

async def main():
    await task_fizzbuzz()

async def task_fizzbuzz():
    for x in range(1, 10):
        print(fizzbuzz(x))
    return None

loop = asyncio.get_event_loop()
# コルーチンでmain関数を呼び出し
loop.run_until_complete(main())
loop.close()
