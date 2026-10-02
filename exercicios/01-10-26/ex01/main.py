class Produto: 
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoDeCompra:
    def __init__ (self, produtos):
        self.produtos = []


    def adicionar_produto(self, prod):
        self.produtos.append(Produto(prod.nome, prod.preco))

    def calcula_total(self, produtos):
        total = 0
        for prod in produtos:
            total = total + prod.preco

        return total
    def exibir(self, produtos):
        for p in produtos:
            print('Nome: {nome}  |  Preço: {preco}')
        print('Total: ', self.calcula_total(produtos))


prods = []
   
p1 = Produto('Bosta', 10)
p2 = Produto('Mijo', 5)


car = CarrinhoDeCompra(prods)

car.adicionar_produto(p1)
car.adicionar_produto(p2)

car.exibir(prods)

   





