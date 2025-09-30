import random
from .logica import jogadas_livres, checar_vencedor, empate


def minimax(jogo, maximizando, simbolo_ia, simbolo_jogador):
    winner, _ = checar_vencedor(jogo)
    if winner == simbolo_ia:
        return 1
    elif winner == simbolo_jogador:
        return -1
    elif empate(jogo):
        return 0

    if maximizando:
        best = -999
        for mv in jogadas_livres(jogo):
            jogo[mv] = simbolo_ia  
            score = minimax(jogo, False, simbolo_ia, simbolo_jogador)
            jogo[mv] = ' '
            if score > best:
                best = score
        return best
    else:
        best = 999
        for mv in jogadas_livres(jogo):
            jogo[mv] = simbolo_jogador
            score = minimax(jogo, True, simbolo_ia , simbolo_jogador)
            jogo[mv] = ' '
            if score < best:
                best = score
        return best


def melhor_jogada_minimax(jogo, simbolo_ia , simbolo_jogador):
    best_score = -999
    best_moves = []
    for mv in jogadas_livres(jogo):
        jogo[mv] = simbolo_ia  
        score = minimax(jogo, False, simbolo_ia, simbolo_jogador)
        jogo[mv] = ' '
        if score > best_score:
            best_score = score
            best_moves = [mv]
        elif score == best_score:
            best_moves.append(mv)
    return random.choice(best_moves) if best_moves else None


def jogada_ia(jogo, dificuldade, simbolo_ia='O', simbolo_jogador='X'):
    r = random.random()
    if dificuldade == 'Fácil':
        return random.choice(jogadas_livres(jogo))
    elif dificuldade == 'Médio':
        if r < 0.5:
            return melhor_jogada_minimax(jogo, simbolo_ia  , simbolo_jogador)
        else:
            return random.choice(jogadas_livres(jogo))
    elif dificuldade == 'Difícil':
        if r < 0.7:
            return melhor_jogada_minimax(jogo, simbolo_ia  , simbolo_jogador)
        else:
            return random.choice(jogadas_livres(jogo))
    elif dificuldade == 'Impossível':
        return melhor_jogada_minimax(jogo, simbolo_ia  , simbolo_jogador)
    else:
        return random.choice(jogadas_livres(jogo))
