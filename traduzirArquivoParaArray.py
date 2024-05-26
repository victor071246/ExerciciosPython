"""Escreva a função palavras() que aceita um argumento de entrada 
— um nome de arquivo — 
e retorna a lista de palavras reais (sem símbolos de pontuação !,.:;?) no arquivo.

>>> palavras('example.txt')

['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',

'the', 'new', 'line', 'character', 'There', 'is', 'a',

'blank', 'line', 'above', 'this', 'line']"""

def palavras(nomearq):
    'retorna a lista de palavras reais, sem pontuação'
    arqEntrada = open(nomearq, 'r')
    conteudo = arqEntrada.read()
    arqEntrada.close
    tabela = str.maketrans('!,.:;?', 6*'')
    conteudo = conteudo.translate(tabela)
    conteudo = conteudo.lower()
    return conteudo.split()