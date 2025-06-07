print("##############")
print("Seja bem vindo ao Cinema Belas Artes")
idade = int(input("Por favor Digite sua idade: "))
nome = input("Digite agor o seu nome: ")

print("---------------")
if idade >= 18:
    print(f"Seja bem vindo {nome}, você tem {idade} anos e pode entrar!")
else:
    print(f"sinto muito {nome}, você é menor de idade")
