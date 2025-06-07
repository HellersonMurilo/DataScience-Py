"""
Solicitar o nome do veiculo
Solicitar o preço original do veiculo

Oferecer 3 tipos de descontos
- 60% de desconto
- 30% de desconto
- 0% de desconto
"""

nome_veiculo = input('Insira o nome do veiculo ')
preco_original = float(input('Insira o valor do preço original '))

desconto = int(input('Informe qual desconto voce deseja? 60%, 30% ou 0? '))

match desconto:
    case 60:
        valor_desconto = preco_original * 0.60
        valor_final = preco_original - valor_desconto
    case 30:
        valor_desconto = preco_original * 0.30
        valor_final = preco_original - valor_desconto
    case 0: 
        valor_desconto = preco_original * 0.0
        valor_final = preco_original - valor_desconto
    case _:
        print("Desconto inválido")
        valorFinal = preco_original 

print(f"O veiculo {nome_veiculo} teve o valor final de R$ {valor_final}")
