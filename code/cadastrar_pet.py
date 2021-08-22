import utilidades #arquivo que importa utilidades e ferramentas gerais que vão ser utilizadas em todos os arquivos


def insetir(): # insere o animal ao sistema
    print("inserir")

def remover(): # remove o animal no sistema
    print("remover")

def alterar(): # altera as informações do animal no sistema
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