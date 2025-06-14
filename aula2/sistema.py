def menu():
    print("====================")
    print("Sistema do Café, chá e lasanha SENAI")
    print("====================")
    print("1 - Criar um café")
    print("2 - Listar os cafés")
    print("3 - Qual o maior preço do Café?")
    print("0 - Sair do sistema")

    opcao = int(input("Escolha uma opção: "))
    return opcao


# Lista que irá armazenar objetos da classe Cafe
cafes = []


# Definição da classe
class Cafe:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} | R${self.preco:.2f}"


# Loop principal do sistema
while True:
    opcao = menu()

    match opcao:
        case 1:
            nome = input("Digite o nome do café: ")
            preco = float(input("Digite o preço do café: "))

            # Criando o objeto Café
            novo_cafe = Cafe(nome, preco)

            # Salvando na lista
            cafes.append(novo_cafe)

            print("Café registrado com sucesso!\n")

        case 2:
            if not cafes:
                print("Nenhum café na lista\n")
            else:
                print("\n--- Lista de Cafés ---")
                #percorrendo as listas com os objetos
                for cafe in cafes:
                    print(cafe) 
                print()

        case 3:
            if not cafes:
                print("Nenhum café na lista\n")
            else:
                ## A função max() percorre a lista 'cafés' e compara os cafés usando o preço como critério,
                # através da função lambda que extrai o valor da chave 'preco' de cada café.
                mais_caro = max(cafes, key=lambda cafe: cafe.preco)
                print(
                    f"O café mais caro é {mais_caro.nome} custando R$ {mais_caro.preco:.2f}\n"
                )

        case 0:
            print("Sistema encerrado!")
            break

        case _:
            print("Opção inválida. Tente novamente.\n")
