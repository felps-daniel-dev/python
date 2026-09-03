print("Hello, Word!")

print(7 + 3)

print("17" + "12")

nome = "Felipe"
idade = 21
sexo = "Masculino"

print("Nome: ", nome, "Idade: ", idade, "Sexo: ", sexo)

nome = input("Digite seu nome: ")
print("Olá, ", nome)

print("============================================")
print("Digite o dia o mes e o ano do seu aniversário")
dia = input("Dia: ")
mes = input("Mês: ")
ano = input("Ano: ")
idade = 2026 - int(ano)
print(f"Nome: {nome} Nascimento: {dia}/{mes}/{ano}")  ##sempre colocar o f na frente para exibir porque ele vai indentificar o coringa {}
##  para interpretar como variavel e não com string

print("Você tem ", idade, " anos!")
