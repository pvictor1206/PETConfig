

def encontrar_dados_pet():

    dicionario_animais = {}

    cont_dados_pet = 0  # contador que mostra a quantidade de animais dentro do arquivo
    verificacao_tamanho = 0
    lista_pet = []  # lista que onde fica armazenado os animais
    lista_dados_pet = []

    nome_arquivo = ''
    idade_arquivo = ''
    sexo_arquivo = ''
    porte_arquivo = ''
    raca_arquivo = ''
    lar_temp_arquivo = ''
    lar_ante_arquivo = ''
    responsavel_arquivo = ''
    data_adocao_arquivo = ''
    codigo_arquivo = ''  # string onde fica o código


    try:  # verifica se existe dados dentro do arquivo
        dados_pet = open("dados_pet.txt", 'r')

        for dados in dados_pet:  # adiciona todos os animais dentro de uma lista
            lista_pet.append(dados)

        dados_pet.close()

        for linha in lista_pet:  # for em que verifica se existe um codigo para remoção
            for letra in linha:
                if letra == ',':
                    cont_dados_pet += 1
                if cont_dados_pet == 0 and letra != ',':
                    nome_arquivo += letra
                if cont_dados_pet == 1 and letra != ',':
                    idade_arquivo += letra
                if cont_dados_pet == 2 and letra != ',':
                    sexo_arquivo += letra
                if cont_dados_pet == 3 and letra != ',':
                    porte_arquivo += letra
                if cont_dados_pet == 4 and letra != ',':
                    raca_arquivo += letra
                if cont_dados_pet == 5 and letra != ',':
                    lar_temp_arquivo += letra
                if cont_dados_pet == 6 and letra != ',':
                    lar_ante_arquivo += letra
                if cont_dados_pet == 7 and letra != ',':
                    responsavel_arquivo += letra
                if cont_dados_pet == 8 and letra != ',':
                    data_adocao_arquivo += letra
                if cont_dados_pet == 9 and letra != ',':
                    try:
                        if verificacao_tamanho == (len(lista_pet) - 1):
                            if letra == '':
                                continue
                            else:
                                codigo_arquivo += letra
                                break

                        elif (type(int(letra) == int)):
                            codigo_arquivo += letra


                    except:


                        dicionario_animais['nome'] = nome_arquivo
                        dicionario_animais['idade'] = idade_arquivo
                        dicionario_animais['sexo'] = sexo_arquivo
                        dicionario_animais['porte'] = porte_arquivo
                        dicionario_animais['raca'] = raca_arquivo
                        dicionario_animais['lar_temp'] = lar_temp_arquivo
                        dicionario_animais['lar_anterior'] = lar_ante_arquivo
                        dicionario_animais['responsavel'] = responsavel_arquivo
                        dicionario_animais['data_adocao'] = data_adocao_arquivo
                        dicionario_animais['codigo'] = codigo_arquivo

                        lista_dados_pet.append(dicionario_animais)

                        nome_arquivo = ''
                        idade_arquivo = ''
                        sexo_arquivo = ''
                        porte_arquivo = ''
                        raca_arquivo = ''
                        lar_temp_arquivo = ''
                        lar_ante_arquivo = ''
                        responsavel_arquivo = ''
                        codigo_arquivo = ''
                        data_adocao_arquivo = ''
                        verificacao_tamanho += 1
                        cont_dados_pet = 0
                        break


    except:
        print("Nenhum animal cadastrado.")

    return lista_dados_pet


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

