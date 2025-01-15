#import random
import WConio2
import curses

altura = 50
largura = 50
cobra = [(10, 10), (9, 10), (8, 10)] #valores testes
#parte comentada pois ainda terá modificações a fazer
def gerar_comida():
    #comida_x=random.randrange(0, largura) 
    #comida_y=random.randrange(0, altura)
    #return comida_x, comida_y
    pass

def gerar_cobra():
    for i, (x, y) in enumerate(cobra): 
        #stdscr.move(y, x)
        if i == 0:
            WConio2.addstr("o")  
        else:
            WConio2.addstr("=")  
    #stdscr.refresh()

#controle de teclas