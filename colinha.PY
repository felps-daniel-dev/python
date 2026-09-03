# ==========================================
# COLINHA DE SINTAXE DE PYTHON
# ==========================================

# 1. Entradas, Saídas e Variáveis
# Leitura de dados
nome = input("Nome: ")
idade = int(input("Idade: "))
peso = float(input("Peso: "))
# Print formatado (f-string)
print(f"Olá {nome}, {idade} anos, {peso}kg.")

# 2. Operadores Aritméticos
soma = 10 + 5 # Adição (+)
sub = 10 - 5 # Subtração (-)
mult = 10 * 5 # Multiplicação (*)
div = 10 / 5 # Divisão Real (/)
divi = 10 // 3 # Divisão Inteira (//) -> 3
rest = 10 % 3 # Resto/Módulo (%) -> 1
pot = 2 ** 3 # Potência (**) -> 8

# 3. Manipulação de Strings
txt = " Curso de Python "
print(len(txt)) # Tamanho do texto
print(txt.upper()) # MAIÚSCULAS
print(txt.lower()) # minúsculas
print(txt.strip()) # Remove espaços extras
print(txt.replace("Python", "Dev"))
print(txt[2:7]) # Fatiamento [início:fim]

# 4. Condicionais (if / elif / else)
nota = 7.5
if nota >= 7.0:
    print("Aprovado")
elif nota >= 5.0:
    print("Recuperação")
else:
    print("Reprovado")

# 5. Laço Contado (for)
# Repete de 1 a 5 (o 6 não entra)
for c in range(1, 6):
    print(c)

# Percorrendo uma sequência
for item in ["A", "B", "C"]:
    print(item)

# 6. Laço Condicional (while)
c = 1
while c <= 5:
    print(c)
    c += 1 # Incremento

# Loop infinito com parada
while True:
    resp = input("Sair? [S/N]: ").upper()
    if resp == "S":
        break

# 7. Coleções (Tuplas, Listas, Dicts)
# Tupla (Imutável)
tup = (1, 2, 3)

# Lista (Mutável)
lis = [10, 20]
lis.append(30) # Adiciona
lis.pop(0) # Remove por índice
lis.sort() # Ordena

# Dicionário (Chave: Valor)
dico = {"nome": "Ana", "idade": 22}
print(dico["nome"])

# 8. Funções (def)
def somar(a, b):
    res = a + b
    return res

total = somar(5, 10)
print(f"Total da soma: {total}")

# 9. Módulos e Importações
import math
print(math.sqrt(16)) # Raiz quadrada

from random import randint
num = randint(1, 10) # Número aleatório
print(f"Número sorteado: {num}")

# 10. Tratamento de Erros (try / except)
try:
    n = int(input("Número para divisão: "))
    r = 10 / n
except ValueError:
    print("Digite um número válido!")
except ZeroDivisionError:
    print("Não divida por zero!")
else:
    print(f"Resultado: {r}")