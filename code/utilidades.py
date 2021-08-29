
def bibliotecas_pets(nome_pet,idade_pet,sexo_pet,porte_pet,raca_pet,lar_temporario,lar_anterior,responsavel_pet,data_adocao,codigo_pet):
    biblioteca_animais = {
        'nome_pet': nome_pet,
        'idade_pet': idade_pet,
        'sexo_pet': sexo_pet,
        'porte_pet': porte_pet,
        'raca_pet': raca_pet,
        'lar_temporario': lar_temporario,
        'lar_anterior': lar_anterior,
        'responsavel_pet': responsavel_pet,
        'data_adocao': data_adocao,
        'codigo_pet': codigo_pet
    }

    return biblioteca_animais

def encontrar_dados_pet():
    pass


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

