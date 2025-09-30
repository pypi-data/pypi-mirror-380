casos_de_vitoria = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def jogadas_livres(jogo):
    return [i for i, v in enumerate(jogo) if v == ' ']

def empate(jogo):
    return all(v != ' ' for v in jogo)

def checar_vencedor(jogo):
    for a,b,c in casos_de_vitoria:
        if jogo[a] == jogo[b] == jogo[c] and jogo[a] != ' ':
            return jogo[a], (a,b,c)
    return None, None        