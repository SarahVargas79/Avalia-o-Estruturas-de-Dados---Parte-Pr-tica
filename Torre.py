class Torre:
    def __init__(self, id, nome, end):
        self.id = id
        self.nome = nome
        self.end = end

    def __str__(self):
        return f"Torre: \n{self.id} \nNome: {self.nome} \nEndereço: {self.end}"
