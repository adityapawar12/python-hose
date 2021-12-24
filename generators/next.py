def simple_fun():
    for i in range(4):
        yield i

g = simple_fun()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
