from .logica import jogadas_livres, empate, checar_vencedor
from .ia import jogada_ia
from utils.helpers import (
    input_jogador,
    escolher_rounds,
    clear_screen,
    vitoria_o,
    vitoria_x,
    tela_empate,
    placar,
    imprimir_centralizado_vertical
)
from shutil import get_terminal_size
from utils.print_big_board import imprimir_tabuleiro
import time
import re

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

def strip_ansi(text):
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

def center_ansi(text, width):
    visible_length = len(strip_ansi(text))
    padding = width - visible_length
    if padding <= 0:
        return text
    left_padding = padding // 2
    right_padding = padding - left_padding
    return ' ' * left_padding + text + ' ' * right_padding


def rodada_unica(
    modo,
    dificuldade=None,
    jogador_inicial="X",
    rodada_atual=1,
    rodadas_totais=1,
    vitorias_x=0,
    vitorias_o=0,
    empates=0,
):
    jogo = [" "] * 9
    jogador = jogador_inicial

    while True:
        ganhador, destaque = checar_vencedor(jogo)

        linhas = []
        titulo_rodada = f"--------------- Rodada {rodada_atual} de {rodadas_totais} ---------------\n"
        linhas.append(titulo_rodada.center(largura))

        linhas_tabuleiro = imprimir_tabuleiro(jogo, destaque=destaque)
        for linha in linhas_tabuleiro:
            linhas.append(center_ansi(linha, largura))
        linhas.append("\n")
        linhas.extend(placar(modo, vitorias_x, vitorias_o, empates))

        if ganhador:
            linhas.append(f"Vencedor da rodada: {ganhador}".center(largura))
            clear_screen()
            imprimir_centralizado_vertical(linhas)
            time.sleep(5)
            return ganhador

        if empate(jogo):
            linhas.append("Rodada terminou em empate.".center(largura))
            clear_screen()
            imprimir_centralizado_vertical(linhas)
            time.sleep(5)
            return "Empate"

        clear_screen()
        imprimir_centralizado_vertical(linhas)

        if modo == "PvP" or jogador == "X":
            mv = input_jogador(jogador)
            if mv == "quit":
                return "Quit"
            if jogo[mv] != " ":
                print("Posição ocupada.")
                time.sleep(1)
                continue
            jogo[mv] = jogador
        else:
            print("Máquina jogando...")
            mv = jogada_ia(jogo, dificuldade, simbolo_ia="O", simbolo_jogador="X")
            if mv is None:
                moves = jogadas_livres(jogo)
                if not moves:
                    continue
                import random
                mv = random.choice(moves)
            jogo[mv] = "O"

        jogador = "O" if jogador == "X" else "X"


def serie_de_rodadas(modo, dificuldade=None):
    rodadas = escolher_rounds()
    if rodadas is None:
        return None

    vitorias = {"X": 0, "O": 0, "Empate": 0}
    rodadas_necessarias = int(rodadas) // 2 + 1
    jogador_inicial = "X"

    for r in range(1, int(rodadas) + 1):
        clear_screen()
        titulo_rodada = f"--------------- Rodada {r} de {rodadas} ---------------\n"
        imprimir_centralizado_vertical([titulo_rodada.center(largura)])

        resultado = rodada_unica(
            modo,
            dificuldade=dificuldade,
            jogador_inicial=jogador_inicial,
            rodada_atual=r,
            rodadas_totais=int(rodadas),
            vitorias_x=vitorias["X"],
            vitorias_o=vitorias["O"],
            empates=vitorias["Empate"],
        )

        if resultado == "Quit":
            clear_screen()
            print("Jogo interrompido pelo usuário. Voltando ao menu...".center(largura))
            time.sleep(3)
            return None

        if resultado == "X":
            vitorias["X"] += 1
        elif resultado == "O":
            vitorias["O"] += 1
        else:
            vitorias["Empate"] += 1

        if vitorias["X"] >= rodadas_necessarias or vitorias["O"] >= rodadas_necessarias:
            break

        jogador_inicial = "O" if jogador_inicial == "X" else "X"

    clear_screen()
    if vitorias["X"] > vitorias["O"]:
        escolha = vitoria_x()
    elif vitorias["O"] > vitorias["X"]:
        escolha = vitoria_o()
    else:
        escolha = tela_empate()

    if escolha == "menu":
        return None
    else:
        exit(0)