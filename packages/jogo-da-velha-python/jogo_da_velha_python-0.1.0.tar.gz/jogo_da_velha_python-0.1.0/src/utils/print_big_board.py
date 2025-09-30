import shutil
import os
import re

reset = "\033[0m"
negrito = "\033[1m"
amarelo = "\033[33m"
ciano = "\033[36m"
vermelho = "\033[31m"
azul = "\033[34m"
fundo_amarelo = "\033[43m"
preto = "\033[30m"

_ansi_re = re.compile(r"\x1b\[[0-9;]*m")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def _strip_ansi(s: str) -> str:
    return _ansi_re.sub("", s)


def _visible_len(s: str) -> int:
    return len(_strip_ansi(s))


def _center_with_ansi(s: str, width: int) -> str:
    vis = _visible_len(s)
    if vis >= width:
        return s
    pad = (width - vis) // 2
    return " " * pad + s


x_arte = ["\\   /", " \\ / ", "  X  ", " / \\ ", "/   \\"]

o_arte = [" ___ ", "/   \\", "|   |", "\\   /", " --- "]


def celula_vazia(num, largura_celula=8):
    label = str(num)
    return [
        " " * largura_celula,
        " " * largura_celula,
        label.center(largura_celula),
        " " * largura_celula,
        " " * largura_celula,
    ]


def imprimir_tabuleiro(board, destaque=None, largura_celula=7, usar_bordas=True):
    if len(board) != 9:
        raise ValueError("tabuleiro deve ter 9 elementos")

    destaque_set = set(destaque) if destaque else set()
    cell_arts = []

    for idx, val in enumerate(board):
        v = (val or " ").strip()
        if v.upper() == "X":
            art = [line.center(largura_celula) for line in x_arte]
        elif v.upper() == "O":
            art = [line.center(largura_celula) for line in o_arte]
        else:
            art = celula_vazia(idx + 1, largura_celula)

        normed = []
        for line in art:
            visible = _strip_ansi(line).ljust(largura_celula)
            if idx in destaque_set:
                normed.append(f"{fundo_amarelo}{preto}{visible}{reset}")
            else:
                if v.upper() == "X":
                    normed.append(f"{vermelho}{visible}{reset}")
                elif v.upper() == "O":
                    normed.append(f"{azul}{visible}{reset}")
                else:
                    normed.append(visible)
        cell_arts.append(normed)

    linhas = []
    altura_celula = len(cell_arts[0])
    for row in range(3):
        for line_i in range(altura_celula):
            partes = [cell_arts[row * 3 + col][line_i] for col in range(3)]
            if usar_bordas:
                sep_vert = f"{amarelo} │ {reset}"
                row_line = sep_vert.join(partes)
            else:
                row_line = "  ".join(partes)
            linhas.append(row_line)
        if row < 2:
            sep_part = f"{amarelo}{'─' * largura_celula}{reset}"
            if usar_bordas:
                mid = f"{amarelo}─┼─{reset}"
                linhas.append(mid.join([sep_part, sep_part, sep_part]))
            else:
                linhas.append(" " * (3 * largura_celula + 4))

    return linhas
