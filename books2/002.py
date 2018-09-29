
print("違いはステートをもつ！！")

# def my_generator():
#     yield 1
#     yield 2
#     yield 3


# gen1 = my_generator()
# for i in gen1:
#     print(i)

#これはできない！！！
# def my_func():
#     return 1
#     return 2
#     return 3

# func1 = my_func()
# for i in func1:
#     print(i)


def count_up():
    x = 0
    while True:
        yield x
        x += 1

gen2 = count_up()

for i in gen2:
     print(i)
     if i == 5:
             break