import os
import time
import WConio2
from funcoesJogo import * 


# Função para exibir a tela de boas-vindas
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


# Função para listar o ranking
def listar_ranking():
    try:
        with open('ranking.txt', 'r') as arquivo:
            rankings = arquivo.readlines()
            if not rankings:
                print("Ainda não há registros no ranking.\n")
                return
            # Ordenar o ranking por pontuação 
            jogadores = []
            for linha in rankings:
                nome, pontos = linha.strip().split(';')
                jogadores.append((nome, int(pontos)))
            jogadores.sort(key=lambda x: x[1], reverse=True)

            print("\nRanking dos jogadores:")
            count = 1
            for nome, pontos in jogadores:
                print(f"{count}° lugar - {nome}: {pontos} pontos")
                count += 1
    except FileNotFoundError:
        print("Ainda não há registros no ranking.\n")


def salvar_ranking(nome, pontos):
    # Carregar dados existentes
    jogadores = {}
    try:
        with open('ranking.txt', 'r') as arquivo:
            for linha in arquivo:
                try:
                    n, p = linha.strip().split(';')
                    p = int(p)  # Tenta converter a pontuação para inteiro
                    jogadores[n] = p  # Adiciona o jogador ao dicionário
                except ValueError:
                    continue 
    except FileNotFoundError:
        pass  # Se o arquivo não existir, apenas continua

    # Atualizar a pontuação do jogador 
    if nome in jogadores:
        jogadores[nome] = max(jogadores[nome], pontos)
    else:
        jogadores[nome] = pontos

    # Salvar o ranking 
    with open('ranking.txt', 'w') as arquivo:
        for n, p in jogadores.items():
            arquivo.write(f"{n};{p}\n")

# Função do menu principal
def menu():
    bem_vindo()
    nome_jogador = input("Digite seu nome para começar: ").strip()
    while True:
        WConio2.textcolor(WConio2.WHITE)
        print("===== MENU =====")
        print("1 - Jogar")
        print("2 - Ver as regras do jogo")
        print("3 - Ver o ranking")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            os.system('cls')
            WConio2.textcolor(WConio2.GREEN)
            
            pontos = curses.wrapper(main)  
            salvar_ranking(nome_jogador, pontos)  # Salva o ranking após o jogo
            print(f"Game Over, {nome_jogador}! Sua pontuação de {pontos} foi salva no ranking.\n")
            True

        elif opcao == "2":
            WConio2.textcolor(WConio2.YELLOW)
            print("\nRegras do jogo:")
            print("- Use a tecla W para se movimentar para cima, A para se movimentar para a esquerda, S para se movimentar para baixo e D para se movimentar para a direita.")
            print("- Coma os Ó para ganhar pontos.")
            print("- Não colida com as paredes ou com o próprio corpo.\n")
        elif opcao == "3":
            WConio2.textcolor(WConio2.CYAN)
            listar_ranking()
        elif opcao == "4":
            WConio2.textcolor(WConio2.WHITE)
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

        