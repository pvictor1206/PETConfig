import utilidades

def ja_adotado(): # funcao que informa todos os animais já adotados
    # PAULO
    print(f"{utilidades.alterar_cor('roxo')}Animais já adotados (MAIS RECENTE AO MAIS ANTIGO){utilidades.alterar_cor('limpar')}")
    utilidades.linha()

    cont_dados_pet = 0  # contador que mostra a quantidade de animais dentro do arquivo
    verificacao_tamanho = 0  # verifica o tamanho da linha do arquivo
    lista_pet = []  # lista que onde fica armazenado os animais
    lista_dados_pet = []  # lista onde será armazenado os informações do arquivo
    lista_datas = []
    lista_cod_verifi = []
    index = 0
    index_adocao = 0
    cont_data = 0


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
    data_dia = ''
    data_mes = ''
    data_ano = ''
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
                                lista_dados_pet[index]['Lar temporário'] = lar_temp_arquivo
                                lista_dados_pet[index]['Lar Anterior'] = lar_ante_arquivo
                                lista_dados_pet[index]['Responsável'] = responsavel_arquivo
                                lista_dados_pet[index]['Data da Adocao'] = data_adocao_arquivo
                                lista_dados_pet[index]['Código'] = int(codigo_arquivo)

                                if data_adocao_arquivo != '':
                                    lista_datas.append([])
                                    for data in data_adocao_arquivo:
                                        if data == '/':
                                            cont_data += 1

                                        if cont_data == 0 and data != '/':
                                            data_dia += data

                                        if cont_data == 1 and data != '/':
                                            data_mes += data

                                        if cont_data == 2 and data != '/':
                                            data_ano += data
                                    lista_cod_verifi.append(int(codigo_arquivo))
                                    lista_datas[index_adocao].append(int(data_ano))
                                    lista_datas[index_adocao].append(int(data_mes))
                                    lista_datas[index_adocao].append(int(data_dia))
                                    lista_datas[index_adocao].append(int(codigo_arquivo))

                                    index_adocao += 1
                                    data_ano = ''
                                    data_dia = ''
                                    data_mes = ''



                                break

                        elif (type(int(letra) == int)):
                            codigo_arquivo += letra



                    except:

                        lista_dados_pet[index]['Nome'] = nome_arquivo
                        lista_dados_pet[index]['Idade (Meses)'] = int(idade_arquivo)
                        lista_dados_pet[index]['Sexo'] = sexo_arquivo
                        lista_dados_pet[index]['Porte'] = porte_arquivo
                        lista_dados_pet[index]['Raça'] = raca_arquivo
                        lista_dados_pet[index]['Lar temporário'] = lar_temp_arquivo
                        lista_dados_pet[index]['Lar Anterior'] = lar_ante_arquivo
                        lista_dados_pet[index]['Responsável'] = responsavel_arquivo
                        lista_dados_pet[index]['Data da Adocao'] = data_adocao_arquivo
                        lista_dados_pet[index]['Código'] = int(codigo_arquivo)

                        if data_adocao_arquivo != '':
                            lista_datas.append([])
                            for data in data_adocao_arquivo:
                                if data == '/':
                                    cont_data += 1

                                if cont_data == 0 and data != '/':
                                    data_dia += data

                                if cont_data == 1 and data != '/':
                                    data_mes += data

                                if cont_data == 2 and data != '/':
                                   data_ano += data

                            lista_datas[index_adocao].append(int(data_ano))
                            lista_datas[index_adocao].append(int(data_mes))
                            lista_datas[index_adocao].append(int(data_dia))
                            lista_datas[index_adocao].append(int(codigo_arquivo))
                            lista_cod_verifi.append(int(codigo_arquivo))
                            index_adocao += 1
                            cont_data = 0
                            data_ano = ''
                            data_dia = ''
                            data_mes = ''





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



        if len(lista_cod_verifi) == 0:
            print("Nenhum animal adotado")
        else:
            for dados in sorted(lista_datas, reverse=True):
               for info in lista_dados_pet:
                   if info['Código'] == dados[3]:
                       print(f"Nome ------------------- {info['Nome']}")
                       print(f"Idade (Meses) ------------------- {info['Idade (Meses)']}")
                       print(f"Sexo ------------------- {info['Sexo']}")
                       print(f"Porte ------------------- {info['Porte']}")
                       print(f"Raça ------------------- {info['Raça']}")
                       print(f"Lar temporário ------------------- {info['Lar temporário']}")
                       print(f"Lar Anterior ------------------- {info['Lar Anterior']}")
                       print(f"Responsável ------------------- {info['Responsável']}")
                       print(f"Data da Adçcao ------------------- {info['Data da Adocao']}")

                       if info['Responsável'] != '':
                           print(f"{utilidades.alterar_cor('amarelo')}=-{utilidades.alterar_cor('limpar')}" * 40)



    except:
        print("Nenhum animal cadastrado.")
