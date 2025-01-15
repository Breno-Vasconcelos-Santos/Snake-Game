import os
import time
#import cursor
import WConio2
#import InquirerPy

def bem_vindo():
    os.system("cls")
    print("Bem-vindo(a) ao")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
    print(""" ######  ##  ##    #####   ##  ##    # ####            #####    #####   ##   ##   # ####
#######  ### ##   #######  ## ##    #######           #######  #######  ### ###  #######
##       ######   ##   ##  ####     ##                ##       ##   ##  #######  ##
 #####   ######   ##   ##  ####     #######           ##  ###  ##   ##  #######  #######
     ##  ## ###   #######  ## ##     #                ##   ##  #######  ## # ##   #
#######  ##  ##   ##   ##  ##  ##   #######           #######  ##   ##  ##   ##  #######
######   ##  ##   ##   ##  ##   ##   ######            #####   ##   ##  ##   ##   ######""")
    time.sleep(2)
    os.system("cls")

def menu():
    bem_vindo()
    #ainda pensar em mudanças para as cores
    WConio2.textcolor(WConio2.GREEN)
    while True:
        print("===== MENU =====")
        print("1 - Jogar")
        print("2 - Ver as regras do jogo")
        print("3 - Ver o ranking")
        print("4 - Sair")
        opcao = input("Escolha uma opcão: ")

        if opcao == "1":
            WConio2.textcolor(WConio2.WHITE)
            print("Iniciando o jogo")
           #aqui iniciar jogo
            break
        elif opcao == "2":
            print("\nRegras do jogo:")
            print("- Use a tecla W para se movimentar para cima, A para se movimentar para a esquerda, S para se movimentar para baixo e D para se movimentar para a direita.")
            print("- Coma os X para ganhar pontos.")
            print("- Não colida com as paredes ou com o próprio corpo.\n")
        elif opcao == "3":
            print("Ranking dos jogadores: ")
            listar_ranking()

        #aqui usar arquivo para salvar ranking
        elif opcao == "4":
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


def listar_ranking():
    arquivo = open('ranking.txt', 'r')
    rankings = arquivo.readlines()
    count = 1
    for r in rankings:
        print(f"{count}°lugar- Pontos: {r}")
        count +=1
    arquivo.close