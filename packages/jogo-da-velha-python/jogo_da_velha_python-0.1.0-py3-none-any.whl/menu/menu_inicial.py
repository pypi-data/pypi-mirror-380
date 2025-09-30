from core.jogo import serie_de_rodadas
from utils.helpers import escolher_modo, escolher_dificuldade, clear_screen

def menu():
    
    while True:
        clear_screen()
        modo = escolher_modo()

        if modo == 'PvP':
            serie_de_rodadas(modo = 'PvP')
    
        elif modo == 'PvE':
            dificuldade = escolher_dificuldade()
            if dificuldade is not None:
                rodadas = serie_de_rodadas(modo = 'PvE', dificuldade =  dificuldade)
                if rodadas == None:
                    continue
        
        else:
            print("Saindo.........") 
            break 