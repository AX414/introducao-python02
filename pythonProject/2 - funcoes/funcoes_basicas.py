def soma_2(a,b):
    return a+b

def divisao(a,b):
    return a/b

def resto(a,b):
    return a%b

def mult(a,b):
    return a*b


a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
print("------------------------------------------")
print("OPERAÇÕES MATEMÁTICAS:")
print(f"O resultado da soma é: {soma_2(a,b)}")
print(f"O resultado da divisao é: {divisao(a,b)} e o resto é {resto(a,b)}")
print(f"O resultado da multiplicação é: {mult(a,b)}")
print("------------------------------------------")
if(resto(a,b) == 0):
    print("A é múltiplo de B")
