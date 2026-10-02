print("Exercicio 4")

valorCasa = float(input("Valor da Casa..............: "))
salario = float(input("Salario do comprador.......: "))
anos = int(input("Em qunatos anos quer pagar.:"))

prestacao = valorCasa / (anos * 12)

if prestacao <= (salario/100)*30:
    print(f"Emprestimo aprovado com parcelas de {prestacao}")
else:
    print(f"Emprestimo negado! O valor da prestação seria {prestacao}")
