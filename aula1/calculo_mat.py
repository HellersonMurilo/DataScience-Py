import math

def calculaBaskara(a, b, c):
    delta = b**2 - 4 * a * c

    if delta < 0:
        print("A equação não possui raízes reais.")
        return

    raiz_quadrada = math.sqrt(delta) #ou delta **0.5

    x1 = (-b + raiz_quadrada) / (2 * a)
    x2 = (-b - raiz_quadrada) / (2 * a)

    print(f"Resultado: x1 = {x1}; x2 = {x2}")

try:
    a = int(input("Insira o valor de A: "))
    b = int(input("Insira o valor de B: "))
    c = int(input("Insira o valor de C: "))

    if a == 0:
        print("O valor de A deve ser diferente de zero em uma equação do 2º grau.")
    else:
        calculaBaskara(a, b, c)
except ValueError:
    print("Por favor, insira apenas números inteiros.")
