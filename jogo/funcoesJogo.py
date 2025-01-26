import random
import curses
from  display.funcoesDisplay import *
import time

cobra = [(10, 10), (9, 10), (8, 10)] 
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

def main(stdscr):
    contador = 0
    curses.curs_set(0)
    stdscr.timeout(100)
    largura, altura = 30, 15
    cobra = [(10, 10), (9, 10), (8, 10)]
    direcao = 100
    opostos = {119: 115, 115: 119, 97: 100, 100: 97}

    comida = gerar_comida(altura, largura, cobra)
    #desenho da borda do jogo
    desenhar_altura(stdscr, altura, largura)

    while True:
        key = stdscr.getch()  # Recebe a entrada do usuário
        if key in opostos and opostos[direcao] != key:
            direcao = key

        y, x = cobra[0]
        if direcao == 115:  #verifica se é o comando de direção para baixo
            y += 1
        elif direcao == 119:  #verifica se é o comando de direção para cima
            y -= 1
        elif direcao == 97:  #verifica se é o comando de direção para esquerda
            x -= 1
        elif direcao == 100:  #verifica se é o comando de direção para direita
            x += 1

        nova_cabeca = (y, x) #nova posição da cabeça

        if (y <= 0 or y >= altura - 1 or x <= 0 or x >= largura - 1 or nova_cabeca in cobra):
            break  # Colisão com as bordas ou com a própria cobra

        cobra.insert(0, nova_cabeca)

        if nova_cabeca == comida:
            comida = gerar_comida(altura, largura, cobra) # Gera nova comida
            contador += 1
        else:
            cobra.pop()

        stdscr.clear() #limpa a tela
        desenhar_altura(stdscr, altura, largura) #redesenho da borda
        gerar_cobra(stdscr, cobra, direcao) #redesenho da cobra
        desenhar_comida(stdscr, comida)
        stdscr.addstr(16, 1, f"Sua pontuação: {contador}")
        stdscr.refresh()
        time.sleep(0.1)

    
    stdscr.clear()
    stdscr.refresh()

    return contador  
    

