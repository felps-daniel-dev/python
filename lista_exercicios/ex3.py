print("Exercicio 3")

velocidade = int(input("Em qual velocidade: "))
multa = 0.0

if velocidade <= 80:
    print("Velocidade aceita!")
else:
    print("Velocidade acima do limite!")
    multa = 7.00 * (velocidade-80)
    
print(f"A multa é de: {multa}")