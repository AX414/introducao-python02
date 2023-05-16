# É possível utilizar uma condição dentro de outra, basta se atentar a identação

# Definindo uma função para checar a idade
def conferir_idade(idade, nome):
    if idade >= 18:
        print("\nÉ maior de idade")
        if(nome == "Eduardo"):
            print("Eduardo é maior de idade")
        else:
            print(f"{nome} é maior de idade, mas não é o Eduardo")
    else:
        print("\nÉ menor de idade")

idade = int(input("Digite a idade: "))
nome = input("Digite seu primeiro nome:")
nome = nome.lower()
nome = nome.capitalize()
conferir_idade(idade, nome)