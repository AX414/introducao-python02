# Python se preocupa muito com a identação,
# a linguagem não utiliza chaves como C, Java e outras linguagens

# Definindo uma função para checar a idade
def conferir_idade(idade):
    if idade >= 18:
        print("É maior de idade")
    else:
        print("É menor de idade")

idade = int(input("Digite a idade: "))
conferir_idade(idade)