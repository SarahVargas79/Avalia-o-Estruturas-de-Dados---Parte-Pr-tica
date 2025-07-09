from Torre import Torre 

class Apartatamento(Torre):
    def __init__(self, id, num_apt, num_vaga):
        self.id = id
        self.num_apt = num_apt
        self.num_vaga = num_vaga

    def __str__(self):
        return f"Apartamento: \n{self.id} \nTorre: \n{self.id} \nNome: {self.nome} \nEndereço: {self.end} \nNº: {self.num_apt} \nBox: {self.num_vaga}"
