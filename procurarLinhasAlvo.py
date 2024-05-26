"""Implemente a função meuGrep(), que toma como entrada duas strings, 
um nome de arquivo e uma string alvo, e exibe cada linha do arquivo 
que contém a string alvo como uma substring.

>>> meuGrep('example.txt', 'line')

"""

def meuGrep(nomearq, alvo):
    'exibe cada linha do arquivo que contém a string alvo'
    arqEntrada = open(nomearq)
    for linha in arqEntrada:
        if alvo in linha:
            print(linha, end='')