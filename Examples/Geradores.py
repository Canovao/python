def meu_gerador():
    yield 1
    yield 2
    yield 3

gen = meu_gerador()
print(next(gen))
print(next(gen))
print(next(gen))
