
def alterar_cor(cor_escolhida): #Funcao que altera a cor de alguma string
    cor = {
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'roxo': '\033[35m',
        'ciano': '\033[36m',
        'cinza': '\033[37m',
        'limpar': '\033[m'
    }
    return cor[cor_escolhida]


def linha(): #Funcao que retorna um print de uma linha
    print(f"=-"*40)




