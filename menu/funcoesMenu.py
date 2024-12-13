import os
import time
#import cursor
#import Wconio2
#import InquirerPy

#deixar isso?
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
    while True:
        print("===== MENU =====")
        print("1 - Jogar")
        print("2 - Ver as regras do jogo")
        print("3 - Ver o ranking")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Iniciando o jogo")
           #aqui iniciar jogo
            break
        elif opcao == "2":
            print("\nRegras do jogo:")
            print("- Use as setas para movimentar a cobra.")
            print("- Coma os X para ganhar pontos.")
            print("- Não colida com as paredes ou com o próprio corpo.\n")
        elif opcao == "3":
            print("Ranking")
        #aqui usar arquivo para salvar ranking
        elif opcao == "0":
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


