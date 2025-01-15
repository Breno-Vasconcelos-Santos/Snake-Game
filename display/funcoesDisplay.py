import curses

def desenhar_largura(stdscr, largura):
    stdscr.addstr("#" * largura + "\n")  # Adiciona a borda no terminal

def desenhar_altura(stdscr, altura, largura):
    if altura > 2 and largura > 2:
        # Parte superior da borda
        desenhar_largura(stdscr, largura)
        
        # Laterais
        for _ in range(altura - 2):
            stdscr.addstr("#" + " " * (largura - 2) + "#\n")
        
        # Parte inferior da borda
        desenhar_largura(stdscr, largura)
    else:
        stdscr.addstr("Dimensões inválidas para a borda.\n")

   