def desenhar_largura(largura):
    print("#" * largura)

def desenhar_altura(altura, largura):
    if altura > 2:  
        # desenha a parte superior da borda
        desenhar_largura(largura)
        
        # desenha as laterais da borda
        for i in range(altura - 2):
            print("#" + " " * (largura - 2) + "#")
        
        # desenha a parte inferior da borda
        desenhar_largura(largura)
