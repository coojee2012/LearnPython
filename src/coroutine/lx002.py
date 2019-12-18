def my_generator():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
g=my_generator()
g.send(None)
print(next(g))
print(next(g))
print('-------------------------')
try:
    g.throw(StopIteration)
except StopIteration:
    print('StopIteration Error')
print('last',next(g))