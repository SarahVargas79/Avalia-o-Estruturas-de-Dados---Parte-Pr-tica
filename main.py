import os
from Fila import Fila

fila = Fila()

op = -1

while op != 0:
    os.system("cls")
    print("--------------------------")
    print("1 - Cadastrar Apartamento")
    print("2 - Remover")
    print("3 - Imprimir Fila de Espera")
    print("0 - Sair")
    op = int(input("Digite sua opção: "))
    print("--------------------------")
    if op == 1:
        print("\n--- Insira os dados ---")
        id = input("ID do apartamento: ")
        num_apt = input("Nº do apartamento: ")
        num_vaga = input("Nº do box do apartamento: ")
        torre = input("Torre do apartamento: ")
        nome = input("Nome da Torre do apartamento: ")
        end = input("Endereço da Torre do apartamento: ")
        fila.cadastrarApt(id, num_apt, num_vaga, torre, nome, end)
    elif op == 2:
        fila.remover()
    elif op == 3:
        fila.imprimir()
    elif op != 0:
        print("Opção inválida!")
    input("Enter para continuar...")
