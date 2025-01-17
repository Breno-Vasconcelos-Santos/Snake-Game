import time
from funcoesJogo import *
from  display.funcoesDisplay import *


def main(stdscr):
    curses.curs_set(0) 
    stdscr.timeout(100)
    largura, altura = 30, 15
    cobra = [(10, 10), (9, 10), (8, 10)]
    direcao = 100 #terminal não estava reconhecendo as teclas, tive que definir assim para reconhece-las, depois ver se tem como melhorar
    opostos = {119: 115, 115: 119, 97: 100, 100: 97}

    #desenho da borda do jogo
    desenhar_altura(stdscr, altura, largura)

    while True:
        key = stdscr.getch() #comando de entrada do usuario
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
            break #verifica se colidiu com si mesmo ou com as bordas
        
        cobra.insert(0, nova_cabeca) #insersão da cabeça agora
        
        cobra.pop()
        
        stdscr.clear() #limpa a tela
        desenhar_altura(stdscr, altura, largura) #redesenho da borda
        gerar_cobra(stdscr, cobra) #redesenho da cobra
        
        time.sleep(0.1)

    stdscr.clear()
    stdscr.addstr(altura // 2, largura // 2 - 5, "Game Over!")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)