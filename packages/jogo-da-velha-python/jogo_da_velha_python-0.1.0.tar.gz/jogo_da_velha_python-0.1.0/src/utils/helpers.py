import os
from shutil import get_terminal_size


def clear_screen():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass


reset = "\033[0m"
negrito = "\033[1m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
magenta = "\033[35m"
ciano = "\033[36m"
branco = "\033[37m"
largura = get_terminal_size().columns


def imprimir_centralizado_vertical(linhas):
    altura_term = get_terminal_size().lines
    n_linhas = len(linhas)
    padding_top = max(0, (altura_term - n_linhas) // 2)
    print("\n" * padding_top, end="")
    largura_term = get_terminal_size().columns
    for linha in linhas:
        print(linha.center(largura_term))


def escolher_modo():

    titulo = r"""
   $$$$$\                                           $$\                                      $$\ $$\                 
   \__$$ |                                          $$ |                                     $$ |$$ |                
      $$ | $$$$$$\   $$$$$$\   $$$$$$\         $$$$$$$ | $$$$$$\        $$\    $$\  $$$$$$\  $$ |$$$$$$$\   $$$$$$\  
      $$ |$$  __$$\ $$  __$$\ $$  __$$\       $$  __$$ | \____$$\       \$$\  $$  |$$  __$$\ $$ |$$  __$$\  \____$$\ 
$$\   $$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |      $$ /  $$ | $$$$$$$ |       \$$\$$  / $$$$$$$$ |$$ |$$ |  $$ | $$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |        \$$$  /  $$   ____|$$ |$$ |  $$ |$$  __$$ |
\$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$  |      \$$$$$$$ |\$$$$$$$ |         \$  /   \$$$$$$$\ $$ |$$ |  $$ |\$$$$$$$ |
 \______/  \______/  \____$$ | \______/        \_______| \_______|          \_/     \_______|\__|\__|  \__| \_______|
                    $$\   $$ |                                                                                       
                    \$$$$$$  |                                                                                       
                     \______/                                                                                        
    """
    linhas = []
    for linha in titulo.splitlines():
        linhas.append(f"{negrito}{ciano}{linha.center(largura)}{reset}")

    linhas.append(f"{ciano}{"1 - Multiplayer (PvP)".center(largura)}{reset}")
    linhas.append(f"{ciano}{"2 - Contra a máquina (PvE)".center(largura)}{reset}")
    linhas.append(f"{vermelho}{"Q - Sair".center(largura)}{reset}")

    imprimir_centralizado_vertical(linhas)
    while True:
        escolha = (
            input(f"\n{amarelo}Escolha o modo (1/2) ou Q para sair: {reset}")
            .strip()
            .upper()
        )

        if escolha == "1":
            return "PvP"
        elif escolha == "2":
            return "PvE"
        elif escolha == "Q":
            return "Quit"
        else:
            print(f"{vermelho}Escolha inválida! Tente novamente...{reset}")


def escolher_rounds():
    titulo = r"""
______          _           _           
| ___ \        | |         | |          
| |_/ /___   __| | __ _  __| | __ _ ___ 
|    // _ \ / _` |/ _` |/ _` |/ _` / __|
| |\ \ (_) | (_| | (_| | (_| | (_| \__ \
  \_| \_\___/ \__,_|\__,_|\__,_|\__,_|___/  
"""
    linhas = []
    for linha in titulo.splitlines():
        linhas.append(f"{negrito}{ciano}{linha.center(largura)}{reset}")

    linhas.append(f"\n{verde}{'1 - Melhor de 1'.center(largura)}{reset}")
    linhas.append(f"{amarelo}{'2 - Melhor de 3'.center(largura)}{reset}")
    linhas.append(f"{magenta}{'3 - Melhor de 5'.center(largura)}{reset}")
    linhas.append(f"{vermelho}{'4 - Melhor de 7'.center(largura)}{reset}")
    linhas.append("Q - Voltar para o menu".center(largura))

    clear_screen()
    imprimir_centralizado_vertical(linhas)
    while True:
        rodadas = (
            input(
                f"\n{amarelo}Escolha uma opção (1 - 4) ou volte para o menu (Q): {reset}"
            )
            .strip()
            .lower()
        )
        if rodadas == "1" or rodadas == "2" or rodadas == "3" or rodadas == "4":
            if rodadas == "1":
                return rodadas
            elif rodadas == "2":
                return 3
            elif rodadas == "3":
                return 5
            elif rodadas == "4":
                return 7
        elif rodadas == "q":
            return None
        else:
            print(f"{vermelho}Escolha inválida! Tente novamente...{reset}")


def escolher_dificuldade():
    titulo = r"""
 ______ _  __ _            _     _           _             _____  ___  
|  _  (_)/ _(_)          | |   | |         | |           |_   _|/ _ \ 
| | | |_| |_ _  ___ _   _| | __| | __ _  __| | ___  ___    | | / /_\ \
| | | | |  _| |/ __| | | | |/ _` |/ _` |/ _` |/ _ \/ __|   | | |  _  |
| |/ /| | | | | (__| |_| | | (_| | (_| | (_| |  __/\__ \  _| |_| | | |
|___/ |_|_| |_|\___|\__,_|_|\__,_|\__,_|\__,_|\___||___/  \___/\_| |_/
"""
    linhas = []
    dificuldades = {"1": "Fácil", "2": "Médio", "3": "Difícil", "4": "Impossível"}
    for linha in titulo.splitlines():
        linhas.append(f"{negrito}{ciano}{linha.center(largura)}{reset}")
    linhas.append(f"\n{verde}{'1 - Fácil'.center(largura)}{reset}")
    linhas.append(f"{amarelo}{'2 - Médio'.center(largura)}{reset}")
    linhas.append(f"{magenta}{'3 - Difícil'.center(largura)}{reset}")
    linhas.append(f"{vermelho}{'4 - Impossível'.center(largura)}{reset}")
    linhas.append("Q - Voltar para o menu".center(largura))

    clear_screen()
    imprimir_centralizado_vertical(linhas)
    while True:
        nivel = (
            input(
                f"\n{amarelo}Escolha o nível (1 - 4) ou volte para o menu (Q): {reset}"
            )
            .strip()
            .lower()
        )
        if nivel == "q":
            return None
        elif nivel in dificuldades:
            return dificuldades[nivel]
        else:
            print(f"{vermelho}Escolha inválida! Tente novamente...{reset}")


def input_jogador(sinal):
    while True:

        pos = input(
            f"\n{amarelo}Jogador {sinal}, escolha uma posição (1 - 9), ou saia do jogo (Q): {reset}"
        )
        if pos in "123456789":
            return int(pos) - 1
        elif pos.lower() == "q":
            return "quit"
        else:
            print(f"{vermelho}Escolha inválida! Tente novamente...{reset}")


def vitoria_x():
    ascii_art = r"""
██╗  ██╗    ██╗   ██╗███████╗███╗   ██╗ ██████╗███████╗██╗   ██╗██╗
╚██╗██╔╝    ██║   ██║██╔════╝████╗  ██║██╔════╝██╔════╝██║   ██║██║
 ╚███╔╝     ██║   ██║█████╗  ██╔██╗ ██║██║     █████╗  ██║   ██║██║
 ██╔██╗     ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║     ██╔══╝  ██║   ██║╚═╝
██╔╝ ██╗     ╚████╔╝ ███████╗██║ ╚████║╚██████╗███████╗╚██████╔╝██╗
╚═╝  ╚═╝      ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝ ╚═════╝ ╚═╝
"""
    linhas = []
    for linha in ascii_art.splitlines():
        linhas.append(f"{azul}{linha.center(largura)}{reset}")
    linhas.append("\n" + f"{ciano}{'1 - Voltar para o Menu'.center(largura)}{reset}")
    linhas.append(f"{ciano}{'2 - Sair do jogo'.center(largura)}{reset}")

    clear_screen()
    imprimir_centralizado_vertical(linhas)
    while True:
        escolha = input(f"\n{amarelo}{'Escolha uma opção (1 - 2): '}{reset}").strip()
        if escolha == "1":
            return "menu"
        if escolha == "2":
            return "quit"
        print(f"{amarelo}{'Opção inválida!'}{reset}")


def vitoria_o():
    clear_screen()
    ascii_art = r"""
 ██████╗     ██╗   ██╗███████╗███╗   ██╗ ██████╗███████╗██╗   ██╗██╗
██╔═══██╗    ██║   ██║██╔════╝████╗  ██║██╔════╝██╔════╝██║   ██║██║
██║   ██║    ██║   ██║█████╗  ██╔██╗ ██║██║     █████╗  ██║   ██║██║
██║   ██║    ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║     ██╔══╝  ██║   ██║╚═╝
╚██████╔╝     ╚████╔╝ ███████╗██║ ╚████║╚██████╗███████╗╚██████╔╝██╗
 ╚═════╝       ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝ ╚═════╝ ╚═╝
"""
    linhas = []
    for linha in ascii_art.splitlines():
        linhas.append(f"{azul}{linha.center(largura)}{reset}")
    linhas.append("\n" + f"{ciano}{'1 - Voltar para o Menu'.center(largura)}{reset}")
    linhas.append(f"{ciano}{'2 - Sair do jogo'.center(largura)}{reset}")

    clear_screen()
    imprimir_centralizado_vertical(linhas)

    while True:
        escolha = input(f"\n{amarelo}{'Escolha uma opção (1 - 2): '}{reset}").strip()
        if escolha == "1":
            return "menu"
        if escolha == "2":
            return "quit"
        print(f"{amarelo}{'Opção inválida!'}{reset}")


def tela_empate():
    clear_screen()
    ascii_art = r"""
███████╗███╗   ███╗██████╗  █████╗ ████████╗███████╗
██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
█████╗  ██╔████╔██║██████╔╝███████║   ██║   █████╗  
██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══██║   ██║   ██╔══╝  
███████╗██║ ╚═╝ ██║██║     ██║  ██║   ██║   ███████╗
╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝
"""
    linhas = []
    for linha in ascii_art.splitlines():
        linhas.append(f"{azul}{linha.center(largura)}{reset}")
    linhas.append("\n" + f"{ciano}{'1 - Voltar para o Menu'.center(largura)}{reset}")
    linhas.append(f"{ciano}{'2 - Sair do jogo'.center(largura)}{reset}")

    clear_screen()
    imprimir_centralizado_vertical(linhas)
    while True:
        escolha = input(f"\n{amarelo}{'Escolha uma opção (1 - 2): '}{reset}").strip()
        if escolha == "1":
            return "menu"
        if escolha == "2":
            return "quit"
        print(f"{amarelo}{'Opção inválida!'}{reset}")


def placar(modo, vitoria_x, vitoria_o, empate):

    def criar_caixa(texto, cor, largura_caixa=17):
        texto_centralizado = texto.center(largura_caixa)
        topo = cor + "┌" + "─" * largura_caixa + "┐" + reset
        meio = cor + "│" + texto_centralizado + "│" + reset
        base = cor + "└" + "─" * largura_caixa + "┘" + reset
        return [topo, meio, base]

    caixa_x = f"Jogador (X) = {vitoria_x}"
    caixa_o = None
    if modo == "PvP":
        caixa_o = f"Jogador (O) = {vitoria_o}"
    elif modo == "PvE":
        caixa_o = f"Máquina (O) = {vitoria_o}"
    caixa_empates = f"Empates = {empate}"

    cx = criar_caixa(caixa_x, vermelho)
    co = criar_caixa(caixa_o, azul)
    ce = criar_caixa(caixa_empates, amarelo)

    linhas = []
    for linha in zip(cx, co, ce):
        linhas.append("   ".join(linha).center(largura + 25))
    return linhas
