#import random
import curses

cobra = [(10, 10), (9, 10), (8, 10)] #valores testes
#parte comentada pois ainda terá modificações a fazer
def gerar_comida():
    #comida_x=random.randrange(0, largura) 
    #comida_y=random.randrange(0, altura)
    #return comida_x, comida_y
    pass

def gerar_cobra(stdscr, cobra):
    for i, (y, x) in enumerate(cobra): 
        stdscr.move(y, x)
        if i == 0:
            stdscr.addstr("O")  
        else:
            stdscr.addstr("x")  
    stdscr.refresh()
#controle de teclas

def gerar_cobra(stdscr, cobra, direcao):
    for i, (y, x) in enumerate(cobra): 
        stdscr.move(y, x)
        
        # Se for a cabeça da cobra (primeiro elemento), desenha o caractere conforme a direção
        if i == 0:
            if direcao == 115:  # Para cima
                stdscr.addstr("^")
            elif direcao == 119:  # Para baixo
                stdscr.addstr("v")
            elif direcao == 97:  # Para esquerda
                stdscr.addstr(">")
            elif direcao == 100:  # Para direita
                stdscr.addstr("<")
        else:
            stdscr.addstr("x")  # Corpo da cobra (todos os outros segmentos)

    stdscr.refresh()