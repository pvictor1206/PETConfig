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


    except:
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


def remover(): # remove o animal no sistema
    # NICOLAS
    codigo_existente = False
    cont_dados_pet = 0 #contador que mostra a quantidade de animais dentro do arquivo
    verificacao_tamanho = 0
    lista_pet = [] # lista que onde fica armazenado os animais
    codigo_arquivo = '' # string onde fica o código


    try: # verifica se existe dados dentro do arquivo
        dados_pet = open("dados_pet.txt", 'r')


        for dados in dados_pet: # adiciona todos os animais dentro de uma lista
            lista_pet.append(dados)

        dados_pet.close()

        codigo_pet = int(input("Código do animal para remoção: ")) # entrada em que o usuário digite o código para alteração

        for linha in lista_pet: # for em que verifica se existe um codigo para remoção
            for letra in linha:
                if letra == ',':
                    cont_dados_pet += 1
                if cont_dados_pet == 9 and letra != ',':
                    try:
                        if verificacao_tamanho == (len(lista_pet) - 1):
                            if letra == '':
                                continue
                            else:
                                codigo_arquivo += letra
                                if str(codigo_pet) == codigo_arquivo:
                                    print(f'Tem certeza que quer remover o animal {codigo_pet}?')
                                    codigo_existente = True

                        elif (type(int(letra) == int)):
                            codigo_arquivo += letra


                    except:

                        if str(codigo_pet) == codigo_arquivo:
                            print(f'Tem certeza que quer remover o animal {codigo_pet}?')
                            codigo_existente = True


                        codigo_arquivo = ''
                        verificacao_tamanho += 1
                        cont_dados_pet = 0
                        break

        if codigo_existente ==  False:
            print("Código não encontrado.")


        #dados_pet = open("dados_pet.txt", 'w')

    except:
        print("Nenhum animal cadastrado.")



def alterar(): # altera as informações do animal no sistema
    # PAULO
    print("alterar")



def cadastrar(): # Funcao principal do arquivo, serve para cadastrar, remover e alterar informações do animal

    while True: #laço infinito até o usuário quiser sair.
        print(f"{utilidades.alterar_cor('roxo')}CADASTRO/REMOVER ANIMAL{utilidades.alterar_cor('limpar')}")

        print(f"{utilidades.alterar_cor('amarelo')}1. Inserir animal{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}2. Remover animal{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}3. Alterar animal{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}4. Sair{utilidades.alterar_cor('limpar')}")

        utilidades.linha()  # insere uma linha na tela

        opcao = int(input(
            f"{utilidades.alterar_cor('verde')}Digite uma das opções: {utilidades.alterar_cor('limpar')}"))  # Lê a opção que será escolhida pelo usuário

        if opcao == 1:
            utilidades.linha()  # insere uma linha na tela
            insetir() # chama a funcao para inserir um animal

        elif opcao == 2:
            utilidades.linha()  # insere uma linha na tela
            remover() # chama a funcao para remover o animal

        elif opcao == 3:
            utilidades.linha()  # insere uma linha na tela
            alterar() # chama a funcao para alterar o animal

        elif opcao == 4: # apenas vai para o menu principal
            break

        else:
            utilidades.linha()  # insere uma linha na tela
            print(
                f"{utilidades.alterar_cor('vermelho')}Opção Inválida, Digite novamente.{utilidades.alterar_cor('limpar')}")
            utilidades.linha()  # insere uma linha na tela