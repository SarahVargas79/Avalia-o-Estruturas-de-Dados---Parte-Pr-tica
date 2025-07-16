import os
from Fila import Fila

fila = Fila()

op = -1

while op != 0:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 40)
    print(" GARAGEM PRIVADA - FILA DE ESPERA ")
    print("=" * 40)
    print("Selecione uma opção:")
    print("1 - Cadastrar Apartamento")
    print("2 - Remover Apartamento da Fila")
    print("3 - Imprimir Fila de Espera")
    print("0 - Sair")
    print("-" * 40)
    op = int(input("Digite sua opção: "))
    print("-" * 40)
    if op == 1:
        print("\n CADASTRO DE APARTAMENTO ")
        print("-" * 40)
        id = input("ID do apartamento: ")
        num_apt = input("Nº do apartamento: ")
        num_vaga = input("Nº da vaga (box): ")
        torre_id = input("ID da Torre: ")
        nome_torre = input("Nome da Torre: ")
        end_torre = input("Endereço da Torre: ")
        fila.cadastrarApt(id, num_apt, num_vaga,
                          torre_id, nome_torre, end_torre)
    elif op == 2:
        print("\nREMOVER APARTAMENTO DA FILA...\n")
        fila.remover()
    elif op == 3:
        print("\nIMPRIMIR FILA DE ESPERA...\n")
        fila.imprimir()
    elif op != 0:
        print("\nOpção inválida! Tente novamente.")
    input("Pressione ENTER para continuar...")
    print("\nObrigado por utilizar o sistema de fila de espera!")
    print("Até logo!")
