print("Exercicio 7")

lista = []
while True:
    novoValor = input("Novo valor: ")
    if novoValor == "SAIR":
        break
    else:
        if novoValor not in lista: #se o novo valor não tiver na lista1
            lista.append(novoValor)
        
    
print(lista)