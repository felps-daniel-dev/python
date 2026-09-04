class Carro:
    nome: str
    ano: int
    def __init__(self,nome, ano ):
        self.nome = nome
        self.ano = ano

car2: Carro = Carro("bosta", 1990)
car: Carro = Carro("bosta", 1990)