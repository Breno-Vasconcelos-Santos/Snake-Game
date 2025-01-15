#import random
import WConio2
import curses

altura , largura=50
cobra = [(10, 10), (9, 10), (8, 10)] #valores testes
#parte comentada pois ainda terá modificações a fazer
def gerar_comida():
    #comida_x=random.randrange(0, largura) 
    #comida_y=random.randrange(0, altura)
    #return comida_x, comida_y
    pass

def gerar_cobra(stdscr, cobra):
    for i, (x, y) in enumerate(cobra): 
        stdscr.move(y, x)
        if i == 0:
            stdscr.addstr("o")  
        else:
            stdscr.addstr("=")  
    stdscr.refresh()



#controle de teclas