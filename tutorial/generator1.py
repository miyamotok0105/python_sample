def gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
g1 = gen()
print(g1)
print(next(g1))
print(next(g1))

print(list(g1))

