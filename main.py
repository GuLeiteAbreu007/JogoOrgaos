# importando bibliotecas
import unidecode
import pandas as pd
import os
import random

# mudando lugar da execução para a pasta do projeto
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def gerarPerguntaFuncao(num: int, descricao: str, orgao: str, numPerguntas: int) -> None:
    '''
    Entradas:
        num - número da questão
        descricao - descrição/dica do órgão
        orgao - resposta de qual órgão é
        numPerguntas - total do número de questões
    
    Pega uma pergunta e printa na tela se o usuário acertou. Não deixa o usuário sair da pergunta enquanto ele não acertar

    '''
    if unidecode.unidecode(input(f'\nÓrgão {num}/{numPerguntas}:\n{descricao}\nDigite o órgão: ')).lower().strip() == unidecode.unidecode(orgao).lower().strip():
        print('Parabéns! Você acertou!')

    else:
        while True:
            print('Errou...')
            if unidecode.unidecode(input(f'Digite novamente: ')).lower().strip() == unidecode.unidecode(orgao).lower().strip():
                print('Parabéns! Você acertou!')
                break

            
# lendo tabelas de perguntas
tabela = pd.read_excel('tabelaOrgaos.xlsx')

# inicializando listas
listaDescricao = []
listaOrgaos = []

# preenchendo listas
for descricao, orgao in zip(tabela['Função'], tabela['Órgão']):
    listaDescricao.append(descricao)
    listaOrgaos.append(orgao)

print('\n\n----------------Jogo!-----------------')

while True:
    # gera uma ordem aleatória de perguntas
    ordem = []
    i = 0
    while i != 10:
        num = random.randint(0, 9)
        if num not in ordem:
            ordem.append(num)
            i += 1
            
        else:
            pass 

    # gera a pergunta
    for num, c in enumerate(ordem):
        gerarPerguntaFuncao(num + 1, listaDescricao[c], listaOrgaos[c], len(listaDescricao))

    print('\nFim do jogo!')

    # pergunta para sair do jogo
    if unidecode.unidecode(input(f'\nDeseja sair? (s/n): ')).lower().strip() == 's':
        break