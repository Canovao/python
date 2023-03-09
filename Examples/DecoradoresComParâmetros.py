def meu_decorador_com_argumentos(arg1, arg2):
    def decorador(funcao):
        def funcao_decorada(*args, **kwargs):
            print(f"Argumentos do decorador: {arg1}, {arg2}")
            resultado = funcao(*args, **kwargs)
            return resultado
        return funcao_decorada
    return decorador

@meu_decorador_com_argumentos("arg1", "arg2")
def minha_funcao_com_argumentos(x, y):
    return x + y

resultado = minha_funcao_com_argumentos(3, 4)
print(resultado)
