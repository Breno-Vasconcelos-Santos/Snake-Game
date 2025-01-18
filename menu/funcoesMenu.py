import os
import time
import WConio2

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
           
    except FileNotFoundError:
        print("Ainda não há registros no ranking.\n")



# Função para salvar o ranking
def salvar_ranking(nome, pontos):
    # Carregar dados existentes
    jogadores = {}
    try:
        with open('ranking.txt', 'r') as arquivo:
            for linha in arquivo:
                n, p = linha.strip().split(';')
                jogadores[n] = int(p)
    except FileNotFoundError:
        pass

            

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
            WConio2.textcolor(WConio2.GREEN)
            print("Iniciando o jogo...")
            # Simulação de pontuação
            pontos = int(input("Digite a pontuação do jogador (para teste): "))
            salvar_ranking(nome_jogador, pontos)
            print(f"Parabéns, {nome_jogador}! Sua pontuação de {pontos} foi salva no ranking.\n")
            break
        elif opcao == "2":
            WConio2.textcolor(WConio2.YELLOW)
            print("\nRegras do jogo:")
            print("- Use a tecla W para se movimentar para cima, A para se movimentar para a esquerda, S para se movimentar para baixo e D para se movimentar para a direita.")
            print("- Coma os X para ganhar pontos.")
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
