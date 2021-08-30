import utilidades #arquivo que importa utilidades e ferramentas gerais que vão ser utilizadas em todos os arquivos

import adotar_pet #arquivo que importa as funcoes para adotar o animal
import ja_adotado_pet #arquivo que importa as funcoes para mostras as informações dos animais já adotados
import cadastrar_pet
import  consultar

utilidades.linha() #insere uma linha na tela
print(f"{utilidades.alterar_cor('ciano')}Bem vindo ao PETConfig{utilidades.alterar_cor('limpar')}")

try:

    while True: # Lanço infinito que fica sempre repetindo as informações do menu até o usuario pedir para sair.

        utilidades.linha()  # insere uma linha na tela

        print(f"{utilidades.alterar_cor('roxo')}MENU PRINCIPAL{utilidades.alterar_cor('limpar')}")

        print(f"{utilidades.alterar_cor('amarelo')}1. Cadastrar/Remover animal{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}2. Adotar animal{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}3. Consultar Animais{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}4. Animais já adotados{utilidades.alterar_cor('limpar')}")
        print(f"{utilidades.alterar_cor('amarelo')}5. Sair do sistema{utilidades.alterar_cor('limpar')}")

        utilidades.linha()  # insere uma linha na tela

        opcao = int(input(f"{utilidades.alterar_cor('verde')}Digite uma das opções: {utilidades.alterar_cor('limpar')}"))  # Lê a opção que será escolhida pelo usuário

        if opcao == 1:
            utilidades.linha()  # insere uma linha na tela
            cadastrar_pet.cadastrar()

        elif opcao == 2:
            utilidades.linha()  # insere uma linha na tela
            adotar_pet.condicao_adocao()

        elif opcao == 3:
            utilidades.linha()  # insere uma linha na tela
            consultar.consultar_animais()


        elif opcao == 4:
            utilidades.linha()  # insere uma linha na tela
            ja_adotado_pet.ja_adotado()

        elif opcao == 5:
            utilidades.linha()  # insere uma linha na tela
            print(f"{utilidades.alterar_cor('vermelho')}Saindo do Sistema...{utilidades.alterar_cor('limpar')}")
            break

        else:
            utilidades.linha()  # insere uma linha na tela
            print(f"{utilidades.alterar_cor('vermelho')}Opção Inválida, Digite novamente.{utilidades.alterar_cor('limpar')}")
            utilidades.linha()  # insere uma linha na tela


except Exception as erro: # Se ocorrer algum erro na leitura no menu, aparece uma mensagem de erro e seu tipo.
    print(f"Erro encontrado... {erro.__class__}")





