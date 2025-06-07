"""
Solicitar 4 notas para o usuario
- realizar o calculo da média
 - SE nota > 7 = aprovado
 - ELSE: = reprovado
"""
def nota_media(a1, a2, a3, a4):
    media = (a1 + a2 + a3 + a4) / 4
    
    if media > 7:
        print(f'Nota {media} Aluno aprovado!')
    else: 
        print(f'Nota {media} Aluno Reprovado')

a1 = float(input("insira o valor da primeira nota "))
a2 = float(input("insira o valor da segunda nota "))
a3 = float(input("insira o valor da terceira nota "))
a4 = float(input("insira o valor da quarta nota "))

nota_media(a1, a2, a3, a4)
