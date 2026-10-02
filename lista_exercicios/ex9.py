
def verificaIdade(resp):
    val = 2026-resp
    if val < 16:
        print(f"Idade ainda não vota! {val} anos")
    elif val > 16 and val <= 17 or val >= 65:
        print(f"Seu voto é opcional! {val} anos")
    else:
        print(f"Seu voto é obrigatório! {val} anos")
        
        
        
        
        
print("Exercicio 9")

resp = input("Ano de nascimento: ")
resp = int(resp)
verificaIdade(resp)


         
    
    