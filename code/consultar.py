import utilidades


def consultar_animais():
    print(f"{utilidades.alterar_cor('roxo')}Consulta de Animais ainda não cadastrados (ordem decrescente de idade){utilidades.alterar_cor('limpar')}")
    utilidades.linha()

    cont_dados_pet = 0  # contador que mostra a quantidade de animais dentro do arquivo
    verificacao_tamanho = 0  # verifica o tamanho da linha do arquivo
    lista_pet = []  # lista que onde fica armazenado os animais
    lista_dados_pet = []  # lista onde será armazenado os informações do arquivo
    lista_ordenar_idade = []  # lista onde estará a idade para ordernar
    index = 0

    # variáveis onde será armazenada as informações dos arquivos
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
            lista_dados_pet.append({})

        dados_pet.close()

        for linha in lista_pet:
            '''
            laço em que analisa todos os dados dentro do arquivo e armazena dentro de uma lista com um dicionário.

            Ex:
            lista_dados_pet[

            {
            'nome': ---
            'idade': ---
            ...
            'codigo': ---

            },
            ...
            {
            'nome': ---
            'idade': ---
            ...
            'codigo': ---

            }


            ]


            '''
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
                                lista_dados_pet[index]['Nome'] = nome_arquivo
                                lista_dados_pet[index]['Idade (Meses)'] = int(idade_arquivo)
                                lista_dados_pet[index]['Sexo'] = sexo_arquivo
                                lista_dados_pet[index]['Porte'] = porte_arquivo
                                lista_dados_pet[index]['Raça'] = raca_arquivo
                                lista_dados_pet[index]['Lar Temporário'] = lar_temp_arquivo
                                lista_dados_pet[index]['Onde o Animal Está'] = lar_ante_arquivo
                                lista_dados_pet[index]['Responsável'] = responsavel_arquivo
                                lista_dados_pet[index]['Data da Adocao'] = data_adocao_arquivo
                                lista_dados_pet[index]['Código'] = int(codigo_arquivo)

                                if lista_dados_pet[index]["Responsável"] == '':
                                    lista_ordenar_idade.append(int(idade_arquivo))


                                break

                        elif (type(int(letra) == int)):
                            codigo_arquivo += letra


                    except:

                        lista_dados_pet[index]['Nome'] = nome_arquivo
                        lista_dados_pet[index]['Idade (Meses)'] = int(idade_arquivo)
                        lista_dados_pet[index]['Sexo'] = sexo_arquivo
                        lista_dados_pet[index]['Porte'] = porte_arquivo
                        lista_dados_pet[index]['Raça'] = raca_arquivo
                        lista_dados_pet[index]['Lar Temporário'] = lar_temp_arquivo
                        lista_dados_pet[index]['Onde o Animal Está'] = lar_ante_arquivo
                        lista_dados_pet[index]['Responsável'] = responsavel_arquivo
                        lista_dados_pet[index]['Data da Adocao'] = data_adocao_arquivo
                        lista_dados_pet[index]['Código'] = int(codigo_arquivo)

                        if lista_dados_pet[index]["Responsável"] == '':
                            lista_ordenar_idade.append(int(idade_arquivo))

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
                        index += 1
                        cont_dados_pet = 0
                        break


        lista_ordenar_idade = sorted(lista_ordenar_idade,reverse=True)
        aux_idade = len(lista_ordenar_idade)



        if len(lista_ordenar_idade) == 0:
            print("Nenhum animal disponível")
        else:
            for idade in lista_ordenar_idade:
                for dados in lista_dados_pet:
                    if idade == int(dados["Idade (Meses)"]) and aux_idade > 0:
                        for k, v in dados.items():
                            print(f"{k} ------------------- {v}")
                            aux_idade -= 1
                        if lista_dados_pet[aux_idade]["Responsável"] == '':
                            print(f"{utilidades.alterar_cor('amarelo')}=-{utilidades.alterar_cor('limpar')}" * 40)





    except:
        print("Nenhum animal cadastrado.")
