import utilidades


def insetir(): # insere o animal ao sistema
    # NICOLAS E PAULO

    resonsavel_pet = ''
    data_adocao_pet = ''

    codigo_pet = 1 # contador que mostra a quantidade de animais dentro do arquivo

    try:
        dados_pet = open("dados_pet.txt", 'r') #abre o arquivo para leitura
        for quantidade in dados_pet: # insere o código do animal. (Ex: Animal 01: 1, Animal 02: 2, Animal 03: 3...)
            codigo_pet += 1

        codigo_pet = str(codigo_pet) # transforma o codigo em string para colocar no arquivo
        dados_pet.close()

        dados_pet = open("dados_pet.txt", 'a')  # abre o arquivo para adicionar conteúdo

        nome_animal = str(input("Nome do Animal: ")).strip().lower()  # digita o nome do animal, tirando os espaços e transformando em letras minusculas

        while True:  # Laço em que verifica se a idade do animal é um numero e se o numero é positivo
            idade_animal = str(input("Idade do animal(meses completos): ")).strip().lower()
            try:
                if int(idade_animal) >= 0:
                    break
                else:
                    print("Idade inválida, Digite novamente")
            except:
                print("Entrada inválida, Digite novamente")

        while True:  # laço que verifica qual o sexo do animal.
            sexo_animal = str(input("Sexo do animal(M-Macho, F-Femia): ")).strip().upper()
            try:
                if sexo_animal == 'F' or sexo_animal == 'M':
                    break
                else:
                    print("Sexo inválido, Digite novamente")
            except:
                print("Entrada inválida, Digite novamente")

        while True:  # laço que verifica qual o por do animal
            porte_animal = str(input("Porte do animal(pequeno,medio,grande): ")).strip().lower()
            try:
                if porte_animal == 'pequeno' or porte_animal == 'medio' or porte_animal == 'grande':
                    break
                else:
                    print("Porto inválido, Digite novamente")
            except:
                print("Entrada inválida, Digite novamente")

        # digitar a raça do animal
        raca_animal = str(input("Raça do animal (caso não tenha, coloque SRD): ")).strip().lower()

        # Digitar o lar temporário
        lar_temporario = str(input("Lar temporário: ")).strip()

        # Digitar o lar anterior
        lar_anterior = str(input("Local onde o animal está: ")).strip()

        dados_pet.write(
            nome_animal + ',' +
            idade_animal + ',' +
            sexo_animal + ',' +
            porte_animal + ',' +
            raca_animal + ',' +
            lar_temporario + ',' +
            lar_anterior + ',' +
            resonsavel_pet + ',' +
            data_adocao_pet + ',' +
            codigo_pet + '\n'
        )

        dados_pet.close()


    except: # se abrir o arquivo e nao existir, vai da erro, então, irá vir para cá...
        codigo_pet = str(codigo_pet)

        dados_pet = open("dados_pet.txt", 'a') # abre o arquivo para adicionar conteúdo

        nome_animal = str(input("Nome do Animal: ")).strip().lower() # digita o nome do animal, tirando os espaços e transformando em letras minusculas

        while True: # Laço em que verifica se a idade do animal é um numero e se o numero é positivo
            idade_animal = str(input("Idade do animal(meses completos): ")).strip().lower()
            try:
                if int(idade_animal) >= 0:
                    break
                else:
                    print("Idade inválida, Digite novamente")
            except:
                print("Entrada inválida, Digite novamente")


        while True: # laço que verifica qual o sexo do animal.
            sexo_animal = str(input("Sexo do animal(M-Macho, F-Femia): ")).strip().upper()
            try:
                if sexo_animal == 'F' or sexo_animal == 'M':
                    break
                else:
                    print("Sexo inválido, Digite novamente")
            except:
                print("Entrada inválida, Digite novamente")

        while True: # laço que verifica qual o por do animal
            porte_animal = str(input("Porte do animal(pequeno,medio,grande): ")).strip().lower()
            try:
                if porte_animal == 'pequeno' or porte_animal == 'medio' or porte_animal == 'grande':
                    break
                else:
                    print("Porto inválido, Digite novamente")
            except:
                print("Entrada inválida, Digite novamente")

        # digitar a raça do animal
        raca_animal = str(input("Raça do animal (caso não tenha, coloque SRD): ")).strip().lower()

        # Digitar o lar temporário
        lar_temporario = str(input("Lar temporário: ")).strip()

        # Digitar o lar anterior
        lar_anterior = str(input("Onde o animal está: ")).strip()

        dados_pet.write(
            nome_animal + ',' +
            idade_animal + ',' +
            sexo_animal + ',' +
            porte_animal + ',' +
            raca_animal + ',' +
            lar_temporario + ',' +
            lar_anterior + ',' +
            resonsavel_pet + ',' +
            data_adocao_pet + ',' +
            codigo_pet + '\n'
        )

        dados_pet.close()


def remover(): # remove o animal no sistema
    # NICOLAS (deixa tudo '')
    print(f"{utilidades.alterar_cor('roxo')}Remoção de Animal{utilidades.alterar_cor('limpar')}")
    utilidades.linha()

    cont_dados_pet = 0  # contador que mostra a quantidade de animais dentro do arquivo
    verificacao_tamanho = 0  # verifica o tamanho da linha do arquivo
    lista_pet = []  # lista que onde fica armazenado os animais
    lista_dados_pet = []  # lista onde será armazenado os informações do arquivo
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
            if ',' in dados:  # Ve se existe conteúdo na linha
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

        if len(lista_dados_pet) == 0:
            print("Nenhum animal cadastrado")
        else:
            for dados in lista_dados_pet:
                for k, v in dados.items():
                    print(f"{k} ------------------- {v}")
                print(f"{utilidades.alterar_cor('amarelo')}=-{utilidades.alterar_cor('limpar')}" * 40)

        escolha_pet = int(input(f"{utilidades.alterar_cor('ciano')}Digite o código do animal para excluir: {utilidades.alterar_cor('limpar')}"))

        for dados in lista_dados_pet:
            if dados['Código'] == escolha_pet:

                utilidades.linha()

                print(f"{utilidades.alterar_cor('verde')}REMOVER ANIMAL{utilidades.alterar_cor('limpar')}")

                print(f"1. Nome ------------------- {dados['Nome']}")
                print(f"2. Idade (Meses) ------------------- {dados['Idade (Meses)']}")
                print(f"3. Sexo ------------------- {dados['Sexo']}")
                print(f"4. Porte ------------------- {dados['Porte']}")
                print(f"5. Raça ------------------- {dados['Raça']}")
                print(f"6. Lar Temporário ------------------- {dados['Lar Temporário']}")
                print(f"7. Onde o Animal Está ------------------- {dados['Onde o Animal Está']}")
                print(f"8. Responsável ------------------- {dados['Responsável']}")
                print(f"9. Data da Adocao' ------------------- {dados['Data da Adocao']}")
                print(
                    f"{utilidades.alterar_cor('vermelho')}Código ------------------- {dados['Código']}{utilidades.alterar_cor('limpar')}")

                arquivo = ''
                contador = 1
                utilidades.linha()

                while True:
                    escolha_alteracao = str(input(f"{utilidades.alterar_cor('ciano')}Tem certeza que quer excluir?(sim/nao) {utilidades.alterar_cor('limpar')}")).strip().lower()
                    try:
                        if escolha_alteracao == 'sim' or escolha_alteracao == 'nao':
                            break
                        else:
                            print("Resposta inválida, Digite novamente")
                    except:
                        print("Resposta inválida, Digite novamente")

                if escolha_alteracao == 'sim':

                    dados_pet = open("dados_pet.txt", 'r')

                    for linha in dados_pet:
                        if contador == escolha_pet:
                            arquivo += '\n'

                        else:
                            arquivo += linha

                        contador += 1

                    dados_pet.close()
                    dados_pet = open("dados_pet.txt", 'w')
                    dados_pet.write(arquivo)
                    print(
                        f"{utilidades.alterar_cor('roxo')}REMOÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()

    except:
        print("Entrada invalida.")



def alterar(): # altera as informações do animal no sistema
    # PAULO
    print(f"{utilidades.alterar_cor('roxo')}Consulta de dados para alteração{utilidades.alterar_cor('limpar')}")
    utilidades.linha()

    cont_dados_pet = 0  # contador que mostra a quantidade de animais dentro do arquivo
    verificacao_tamanho = 0  # verifica o tamanho da linha do arquivo
    lista_pet = []  # lista que onde fica armazenado os animais
    lista_dados_pet = []  # lista onde será armazenado os informações do arquivo
    index = 0

    pet_disponivel = False

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
            if ',' in dados:  # Ve se existe conteúdo na linha
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

        if len(lista_dados_pet) == 0:
            print("Nenhum animal cadastrado")
        else:
            for dados in lista_dados_pet:
                for k,v in dados.items():
                    print(f"{k} ------------------- {v}")
                print(f"{utilidades.alterar_cor('amarelo')}=-{utilidades.alterar_cor('limpar')}" * 40)

        escolha_pet = int(input(f"{utilidades.alterar_cor('ciano')}Digite o código do animal para editar: {utilidades.alterar_cor('limpar')}"))

        for dados in lista_dados_pet:
            if dados['Código'] == escolha_pet:


                utilidades.linha()

                print(f"{utilidades.alterar_cor('verde')}ALTERAR INFORMAÇÕES{utilidades.alterar_cor('limpar')}")

                print(f"1. Nome ------------------- {dados['Nome']}")
                print(f"2. Idade (Meses) ------------------- {dados['Idade (Meses)']}")
                print(f"3. Sexo ------------------- {dados['Sexo']}")
                print(f"4. Porte ------------------- {dados['Porte']}")
                print(f"5. Raça ------------------- {dados['Raça']}")
                print(f"6. Lar Temporário ------------------- {dados['Lar Temporário']}")
                print(f"7. Onde o Animal Está ------------------- {dados['Onde o Animal Está']}")
                print(f"8. Responsável ------------------- {dados['Responsável']}")
                print(f"9. Data da Adocao' ------------------- {dados['Data da Adocao']}")
                print(f"{utilidades.alterar_cor('vermelho')}Código ------------------- {dados['Código']}{utilidades.alterar_cor('limpar')}")

                pet_disponivel = True
                arquivo = ''
                contador = 1
                utilidades.linha()

                escolha_alteracao = int(input(f"{utilidades.alterar_cor('ciano')}Digite o número do item que você quer alterar: {utilidades.alterar_cor('limpar')}"))

                if escolha_alteracao == 1:

                    dados_pet = open("dados_pet.txt", 'r')

                    alterar_nome = str(input("Digite o nome: "))
                    for linha in dados_pet:
                        if contador == escolha_pet:
                            arquivo += alterar_nome
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
                    print(f"{utilidades.alterar_cor('roxo')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()

                elif escolha_alteracao == 2:

                    dados_pet = open("dados_pet.txt", 'r')

                    while True:  # Laço em que verifica se a idade do animal é um numero e se o numero é positivo
                        alterar_idade = int(input("Digite a idade(meses): "))
                        try:
                            if alterar_idade >= 0:
                                break
                            else:
                                print("Idade inválida, Digite novamente")
                        except:
                            print("Entrada inválida, Digite novamente")

                    for linha in dados_pet:
                        if contador == escolha_pet:
                            arquivo += dados['Nome']
                            arquivo += ','
                            arquivo += str(alterar_idade)
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
                    print(f"{utilidades.alterar_cor('roxo')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()

                elif escolha_alteracao == 3:

                    dados_pet = open("dados_pet.txt", 'r')

                    while True:  # laço que verifica qual o sexo do animal.
                        alterar_sexo = str(input("Digite o sexo (M-Macho, F-Femia): ")).strip().upper()
                        try:
                            if alterar_sexo == 'F' or alterar_sexo == 'M':
                                break
                            else:
                                print("Sexo inválido, Digite novamente")
                        except:
                            print("Entrada inválida, Digite novamente")


                    for linha in dados_pet:
                        if contador == escolha_pet:
                            arquivo += dados['Nome']
                            arquivo += ','
                            arquivo += str(dados['Idade (Meses)'])
                            arquivo += ','
                            arquivo += alterar_sexo
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
                    print(f"{utilidades.alterar_cor('roxo')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()

                elif escolha_alteracao == 4:

                    dados_pet = open("dados_pet.txt", 'r')

                    while True:  # laço que verifica qual o por do animal
                        alterar_porte = str(input("Digite  o porte do animal(pequeno,medio,grande): ")).strip().lower()
                        try:
                            if alterar_porte == 'pequeno' or alterar_porte == 'medio' or alterar_porte == 'grande':
                                break
                            else:
                                print("Porto inválido, Digite novamente")
                        except:
                            print("Entrada inválida, Digite novamente")

                    for linha in dados_pet:
                        if contador == escolha_pet:
                            arquivo += dados['Nome']
                            arquivo += ','
                            arquivo += str(dados['Idade (Meses)'])
                            arquivo += ','
                            arquivo += dados['Sexo']
                            arquivo += ','
                            arquivo += alterar_porte
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
                    print(f"{utilidades.alterar_cor('verde')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()

                elif escolha_alteracao == 5:

                    dados_pet = open("dados_pet.txt", 'r')

                    alterar_raca = str(input("Digite a raça: "))

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
                            arquivo += alterar_raca
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
                    print(f"{utilidades.alterar_cor('verde')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()

                elif escolha_alteracao == 6:

                    dados_pet = open("dados_pet.txt", 'r')

                    alterar_lar_temp = str(input("Digite o lar temporário: "))
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
                            arquivo += alterar_lar_temp
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
                    print(f"{utilidades.alterar_cor('verde')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()

                elif escolha_alteracao == 7:

                    dados_pet = open("dados_pet.txt", 'r')

                    onde_esta = str(input("Digite onde está o animal: "))
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
                            arquivo += onde_esta
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
                    print(f"{utilidades.alterar_cor('verde')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()



                elif escolha_alteracao == 8:

                    dados_pet = open("dados_pet.txt", 'r')

                    editar_responsavel = str(input("Digite o responsável: "))
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
                            arquivo += editar_responsavel
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
                    print(f"{utilidades.alterar_cor('verde')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()

                elif escolha_alteracao == 9:

                    dados_pet = open("dados_pet.txt", 'r')

                    data_adocao = str(input("Digite o responsável: "))
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
                            arquivo += data_adocao
                            arquivo += ','
                            arquivo += str(dados['Código'])
                            arquivo += '\n'

                        else:
                            arquivo += linha

                        contador += 1

                    dados_pet.close()
                    dados_pet = open("dados_pet.txt", 'w')
                    dados_pet.write(arquivo)
                    print(f"{utilidades.alterar_cor('verde')}MODIFICAÇÃO REALIZADA COM SUCESSO{utilidades.alterar_cor('limpar')}")
                    dados_pet.close()


                else:
                    print("Entrada invalida")


        if pet_disponivel == False:
            print("Animal não encontrado")

    except:
        print("Entrada invalida.")





def cadastrar(): # Funcao principal do arquivo, serve para cadastrar, remover e alterar informações do animal

    while True: #laço infinito até o usuário quiser sair.
        print(f"{utilidades.alterar_cor('roxo')}CADASTRO/REMOVER ANIMAL{utilidades.alterar_cor('limpar')}")

        print(f"{utilidades.alterar_cor('amarelo')}1. Inserir animal{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}2. Alterar animal{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}3. Remover animal{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}4. Sair{utilidades.alterar_cor('limpar')}")

        utilidades.linha()  # insere uma linha na tela

        opcao = int(input(
            f"{utilidades.alterar_cor('verde')}Digite uma das opções: {utilidades.alterar_cor('limpar')}"))  # Lê a opção que será escolhida pelo usuário

        if opcao == 1:
            utilidades.linha()  # insere uma linha na tela
            insetir() # chama a funcao para inserir um animal

        elif opcao == 2:
            utilidades.linha()  # insere uma linha na tela
            alterar() # chama a funcao para alterar o animal

        elif opcao == 3:
            utilidades.linha()  # insere uma linha na tela
            remover()  # chama a funcao para remover o animal

        elif opcao == 4: # apenas vai para o menu principal
            break

        else:
            utilidades.linha()  # insere uma linha na tela
            print(
                f"{utilidades.alterar_cor('vermelho')}Opção Inválida, Digite novamente.{utilidades.alterar_cor('limpar')}")
            utilidades.linha()  # insere uma linha na tela