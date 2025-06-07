print("Calculadora do SENAI")
print("Digite a operação a realizar")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input(""))
n1 = float(input("Informe o primeiro valor "))
n2 = float(input("Informe o segundo valor "))

match opcao:
    case 1:
        valor = n1 + n2
    case 2:
        valor = n1 - n2
    case 3:
        valor = n1 * n2
    case 4:
        valor = n1 / n2
print(f'o resultado foi de {valor}')

