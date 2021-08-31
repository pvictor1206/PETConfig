import utilidades #arquivo que importa utilidades e ferramentas gerais que vão ser utilizadas em todos os arquivos


def condicao_adocao(): # funcao para verificar as condições para a adoção do animal
    #NICOLAS
    print(f"{utilidades.alterar_cor('roxo')}ADOÇÃO DO PET{utilidades.alterar_cor('limpar')}")
    utilidades.linha()

    while True:
        pergunta01 = str(input(f"Você possui condições financeiras para adotar um novo animal? (Sim/Nao) ")).strip().lower()
        try:
            if pergunta01 == 'sim' or pergunta01 == 'nao':
                break
            else:
                print("Resposta inválida, Digite novamente")
        except:
            print("Resposta inválida, Digite novamente")

    while True:
        pergunta02 = str(input(f"Avaliando sua rotina, você possui tempo livre para se dedicar ao seu novo pet? (Sim/Não)  ")).strip().lower()
        try:
            if pergunta02 == 'sim' or pergunta02 == 'nao':
                break
            else:
                print("Resposta inválida, Digite novamente")
        except:
            print("Resposta inválida, Digite novamente")

    while True:
        pergunta03 = str(input(f"Pense agora no espaço que você possui em casa: qual o porte máximo que o animal deverá ter para viver confortavelmente com você?(Pequeno/Médio/Grande) ")).strip().lower()
        try:
            if pergunta03 == 'pequeno' or pergunta03 == 'medio' or pergunta03 == 'grande':
                break
            else:
                print("Resposta inválida, Digite novamente")
        except:
            print("Resposta inválida, Digite novamente")

    utilidades.linha()

    if pergunta01 == 'sim' and pergunta02 == 'sim':
        adocao_defirida(pergunta03)
    else:
        print("ADOÇÃO INDEFIRIDA")
        #coprovante

def adocao_defirida(pergunta03): # funcao para adotar o animal caso seja defirido nas condições
    #PAULO
    print(f"{utilidades.alterar_cor('roxo')}ADOÇÃO DEFIRIDA: ANIMAIS DISPONIVEIS DE ACORDO COM AS PERGUNTAS{utilidades.alterar_cor('limpar')}")
    utilidades.linha()

    cont_dados_pet = 0  # contador que mostra a quantidade de animais dentro do arquivo
    verificacao_tamanho = 0  # verifica o tamanho da linha do arquivo
    lista_pet = []  # lista que onde fica armazenado os animais
    lista_dados_pet = []  # lista onde será armazenado os informações do arquivo
    pet_disponivel = False

    index = 0
    lista_porte = []


    # variáveis onde será armazenada as informações dos arquivos
    palavra_porte = ''
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

                                if data_adocao_arquivo == '':
                                    for dados in porte_arquivo:
                                        if dados != ',':
                                            palavra_porte += dados

                                    lista_porte.append(palavra_porte)
                                    palavra_porte = ''



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

                        if data_adocao_arquivo == '':
                            for dados in porte_arquivo:
                                if dados != ',':
                                    palavra_porte += dados

                            lista_porte.append(palavra_porte)
                            palavra_porte = ''


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



        if len(lista_porte) == 0:
            print("Nenhum animal disponível")
        else:
            if pergunta03 == 'pequeno':
                for dados in lista_dados_pet:
                    if dados['Porte'] == 'pequeno':
                        if dados['Responsável'] == '':
                            print(f"Nome ------------------- {dados['Nome']}")
                            print(f"Idade (Meses) ------------------- {dados['Idade (Meses)']}")
                            print(f"Sexo ------------------- {dados['Sexo']}")
                            print(f"Porte ------------------- {dados['Porte']}")
                            print(f"Raça ------------------- {dados['Raça']}")
                            print(f"Lar Temporário ------------------- {dados['Lar Temporário']}")
                            print(f"Onde o Animal Está ------------------- {dados['Onde o Animal Está']}")
                            print(f"{utilidades.alterar_cor('vermelho')}Código ------------------- {dados['Código']}{utilidades.alterar_cor('limpar')}")
                            pet_disponivel = True

                            if dados['Responsável'] == '':
                                print(f"{utilidades.alterar_cor('amarelo')}=-{utilidades.alterar_cor('limpar')}" * 40)


            elif pergunta03 == 'medio':
                for dados in lista_dados_pet:
                    if dados['Porte'] == 'pequeno' or dados['Porte'] == 'medio':
                        if dados['Responsável'] == '':
                            print(f"Nome ------------------- {dados['Nome']}")
                            print(f"Idade (Meses) ------------------- {dados['Idade (Meses)']}")
                            print(f"Sexo ------------------- {dados['Sexo']}")
                            print(f"Porte ------------------- {dados['Porte']}")
                            print(f"Raça ------------------- {dados['Raça']}")
                            print(f"Lar Temporário ------------------- {dados['Lar Temporário']}")
                            print(f"Onde o Animal Está ------------------- {dados['Onde o Animal Está']}")
                            print(f"{utilidades.alterar_cor('vermelho')}Código ------------------- {dados['Código']}{utilidades.alterar_cor('limpar')}")
                            pet_disponivel = True


                            if dados['Responsável'] == '':
                                print(f"{utilidades.alterar_cor('amarelo')}=-{utilidades.alterar_cor('limpar')}" * 40)


            elif pergunta03 == 'grande':
                for dados in lista_dados_pet:
                    if dados['Porte'] == 'pequeno' or dados['Porte'] == 'medio' or dados['Porte'] == 'grande':
                        if dados['Responsável'] == '':
                            print(f"Nome ------------------- {dados['Nome']}")
                            print(f"Idade (Meses) ------------------- {dados['Idade (Meses)']}")
                            print(f"Sexo ------------------- {dados['Sexo']}")
                            print(f"Porte ------------------- {dados['Porte']}")
                            print(f"Raça ------------------- {dados['Raça']}")
                            print(f"Lar Temporário ------------------- {dados['Lar Temporário']}")
                            print(f"Onde o Animal Está ------------------- {dados['Onde o Animal Está']}")
                            print(f"{utilidades.alterar_cor('vermelho')}Código ------------------- {dados['Código']}{utilidades.alterar_cor('limpar')}")
                            pet_disponivel = True


                            if dados['Responsável'] == '':
                                print(f"{utilidades.alterar_cor('amarelo')}=-{utilidades.alterar_cor('limpar')}" * 40)


            if pet_disponivel == True:
                escolha_pet = int(input(f"{utilidades.alterar_cor('ciano')}Digite o código do animal para adotar: {utilidades.alterar_cor('limpar')}"))

                pet_disponivel = False

                for dados in lista_dados_pet:
                    if dados['Código'] == escolha_pet:
                        utilidades.linha()

                        responsavel_arquivo = str(input("Nome do responsável: ")).strip()
                        data_adocao_arquivo = str(input("Data da adoção: (dd/mm/aaaa) ")).strip()

                        dados['Responsável'] = responsavel_arquivo
                        dados['Data da Adocao'] = data_adocao_arquivo

                        utilidades.linha()

                        print(f"{utilidades.alterar_cor('verde')}ANIMAL ADOTADO (RECIBO){utilidades.alterar_cor('limpar')}")

                        print(f"Nome ------------------- {dados['Nome']}")
                        print(f"Idade (Meses) ------------------- {dados['Idade (Meses)']}")
                        print(f"Sexo ------------------- {dados['Sexo']}")
                        print(f"Porte ------------------- {dados['Porte']}")
                        print(f"Raça ------------------- {dados['Raça']}")
                        print(f"Lar Temporário ------------------- {dados['Lar Temporário']}")
                        print(f"Onde o Animal Está ------------------- {dados['Onde o Animal Está']}")
                        print(f"Responsável ------------------- {dados['Responsável']}")
                        print(f"Data da Adocao' ------------------- {dados['Data da Adocao']}")
                        print(f"{utilidades.alterar_cor('vermelho')}Código ------------------- {dados['Código']}{utilidades.alterar_cor('limpar')}")
                        pet_disponivel = True

                        dados_pet = open("dados_pet.txt", 'r')

                        arquivo = ''
                        contador = 1

                        for linha in dados_pet:
                            if contador == escolha_pet:
                                arquivo += dados['Nome']
                                arquivo += ','
                                arquivo += str(dados['Idade (Meses)'])
                                arquivo += ','
                                arquivo += dados['Sexo']
                                arquivo += ','
                                arquivo += dados['Porte']
                                arquivo += ','
                                arquivo += dados['Raça']
                                arquivo += ','
                                arquivo += dados['Lar Temporário']
                                arquivo += ','
                                arquivo += dados['Onde o Animal Está']
                                arquivo += ','
                                arquivo += dados['Responsável']
                                arquivo += ','
                                arquivo += dados['Data da Adocao']
                                arquivo += ','
                                arquivo += str(dados['Código'])
                                arquivo += '\n'

                            else:
                                arquivo += linha

                            contador += 1


                        dados_pet.close()

                        dados_pet = open("dados_pet.txt", 'w')

                        dados_pet.write(arquivo)

                        dados_pet.close()




                        print(f"{utilidades.alterar_cor('amarelo')}=-{utilidades.alterar_cor('limpar')}" * 40)

                if pet_disponivel == False:
                    print("Não existe nenhum animal com esse código")




            else:
                print("Nenhum animal disponível")





    except:
        print("Nenhum animal cadastrado.")

