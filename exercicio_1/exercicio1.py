class Veiculo:
    pass

class Carro(Veiculo):
    pass
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def acelerar(self):
        print(f"[self.modelo] esta acelerando!")


my_car = Carro('Voyage', 'Prata')

print("Alo")