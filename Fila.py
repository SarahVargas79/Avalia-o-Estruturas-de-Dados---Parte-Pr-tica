from No import No
from Apartamento import Apartamento
from Torre import Torre


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def cadastrarApt(self, id, num_apt, num_vaga, torre_id, nome_torre, end_torre):
        torre = Torre(torre_id, nome_torre, end_torre)
        apt = Apartamento(id, num_apt, num_vaga, torre)
        nodo = No(apt)

        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo

        print(
            f"\nApartamento ID '{apt.id}' da Torre '{torre.nome}' adicionado na fila de espera!\n"
        )
        self.imprimir()

    def imprimir(self):
        print("Apartamentos na fila de espera:")
        print("-" * 40)
        if self.inicio is None:
            print("Fila de espera vazia!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                print("-" * 42)
                aux = aux.prox

    def remover(self):
        if self.inicio is None:
            print("\nNenhum apartamento na fila de espera.")
        else:
            apt = self.inicio.dado
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            print(
                f"Apartamento ID '{apt.id}' da vaga nº {apt.num_vaga} retirado do box!\n")
            self.imprimir()
