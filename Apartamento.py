from Torre import Torre


class Apartamento:
    def __init__(self, id, num_apt, num_vaga, torre: Torre):
        self.id = id
        self.num_apt = num_apt
        self.num_vaga = num_vaga
        self.torre = torre

    def __str__(self):
        return (
            f"Apartamento ID: {self.id}\n"
            f"Número: {self.num_apt}\n"
            f"Vaga: {self.num_vaga}\n" f"Torre: {self.torre.nome} (ID: {self.torre.id})\n"
            f"Endereço: {self.torre.end}"
        )
