#import random
import curses

cobra = [(10, 10), (9, 10), (8, 10)] #valores testes
#parte comentada pois ainda terá modificações a fazer
def gerar_comida(altura, largura, cobra):
    while True:
        comida_y = random.randint(1, altura - 2)
        comida_x = random.randint(1, largura - 2)
        if (comida_y, comida_x) not in cobra:
            return comida_y, comida_x
        
def desenhar_comida(stdscr, comida):
    y, x = comida
    stdscr.move(y, x)
    stdscr.addstr("Ó")

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
