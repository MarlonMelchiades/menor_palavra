def refazer_funcao():
    print('\nQuer refazer ou quer sair?\n')
    print("\n1.Refazer")
    print("2.Sair")
    opcao = input("\nSelecione uma das opções:")

    if opcao == str(1):
        funcao_principal()
    else:
        print("\nEncerrando o programa... Tchau!\n")


def quantidade(palavra):
    quantidade_de_letras = len(palavra)
    return quantidade_de_letras


def funcao_principal():
    a = input('\nDigite uma palavra...')
    b = input('Digite outra palavra...')

    if quantidade(a) > quantidade(b):
        print('\nA menor palavra é ' + b + ".")
    elif quantidade(a) == quantidade(b):
        print('\nAs duas palavras tem a mesma quantidade de letras.')
    else:
        print('\nA menor palavra é ' + a + ".")
    refazer_funcao()


funcao_principal()
