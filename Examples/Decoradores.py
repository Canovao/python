def meu_decorador(funcao):
    def funcao_decorada():
        print("Antes da execução da função.")
        funcao()
        print("Depois da execução da função.")
    return funcao_decorada

@meu_decorador
def minha_funcao():
    print("Executando minha função.")

minha_funcao()
