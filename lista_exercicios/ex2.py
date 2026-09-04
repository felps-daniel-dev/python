print('Exercicio 2')
nome = input("Digite seu nome: ")

print(nome.upper())
print(nome.lower())
nomeSemEspaco = nome.strip()
qtdFinal = len(nomeSemEspaco)
print(nomeSemEspaco)
print(nome[0: qtdFinal])