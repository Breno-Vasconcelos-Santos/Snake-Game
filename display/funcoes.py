def desenhar_largura(n):
    print("#" * n)

def desenhar_altura(n):
    if n > 2: 
        teste = n - 2
        for i in range(teste):
            print("#" + " " * teste + "#")
