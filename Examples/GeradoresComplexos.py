def meu_gerador_complexo(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

gen = meu_gerador_complexo(10)
for valor in gen:
    print(valor)
