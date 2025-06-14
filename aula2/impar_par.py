"""
O sistema deve pedir um numero E deve dizer se ele é impar ou par
"""

numero = float(input('Informe um número: '))

if (numero % 2) != 0:
    print(f'o numero informado é impar')
else:
    print(f'o numero informado é par')