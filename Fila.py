from No import No
from Apartamento import Apartatamento
from Torre import Torre


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def cadastrarApt(self, id, num_apt, num_vaga, torre):
        apt = Apartatamento(id, num_apt, num_vaga, torre)
        nodo = No(apt)

        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo

        print(
            f"\nVeículo do morador da torre '{torre}', prédio '{apt.id}', nº '{apt.num_apt}' do box '{apt.num_vaga}' adicionado na fila de espera!"
        )
        self.imprimir()

    def imprimir(self):
        print("\n--- GARAGEM PRIVADA - FILA DE ESPERA ---")
        if self.inicio_apts is None:
            print("Fila de espera vazia!")
        else:
            aux = self.inicio_apts
            while aux:
                print(aux.dado)
                aux = aux.prox

    def remover(self):
        if self.inicio is not None:
            print("\nNenhum apartamento na fila de espera.")
        else:
            apt = self.inicio_apts.dado = self.inicio.prox
            self.inicio_apts = self.fim_apts.prox
            print(f"Apartamento da vaga nº: {apt.num_vaga} retirado do box!")
            self.imprimir()
