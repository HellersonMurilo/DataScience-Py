import csv
import os

# biblioteca de graficos
import matplotlib.pyplot as plt

ARQUIVO_CSV = "aula 3\dados_senai.csv"

# verificar se o arquivo existe
arquivo_existe = os.path.exists(ARQUIVO_CSV)


# salvar arquivo
def salvar_em_csv(nome, idade, email):
    # a -> acrescimo
    # newline -> evitar linhas brancas
    # encoding -> Codificação caracteres BR ç, ~, e etc
    with open(ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo)

        # se o arquivo nao existir
        if not arquivo:
            # cria uma nova linha
            escritor.writerow(["nome", "idade", "email"])

        escritor.writerow([nome, idade, email])


def mostrar_grafico():
    # le idades
    faixas = {
        "0-17": 0,
        "18-30": 0,
        "31-45": 0,
        "46-60": 0,
        "60+": 0,
    }

    # mode r -> READ -> Leitura
    with open(
        ARQUIVO_CSV, mode="r", encoding="utf-8"
    ) as arquivo:  ## Abrindo o arquivo e lendo ele
        leitor = csv.DictReader(arquivo)  # salvando os dados, lendo o documento

        # enquanto tiver linhas ele percorre
        for linha in leitor:
            # iterando cada linha da coluna idade, varificando a etapa e somando caso exista
            try:
                idade = int(linha["idade"])
                if idade <= 17:
                    faixas["0-17"] += 1
                elif idade <= 30:
                    faixas["18-30"] += 1
                elif idade <= 45:
                    faixas["31-45"] += 1
                elif idade <= 60:
                    faixas["46-60"] += 1
                else:
                    faixas["60+"] += 1

            # tratamento para caso o valor seja incorreto
            except ValueError:
                continue
            
        #primeiro chave e depois valor
        plt.bar(faixas.keys(), faixas.values(), color='skyblue')
        plt.title('Distribuição por Faixa Etaria')
        plt.xlabel('Faixa Etaria')
        plt.ylabel('Quantidade de Pessoas')
        
        #linhas do grid (True)
        #tracejado e largura
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout() # Finaliza o layout
        plt.show()

# função principal
def main():
    # repetir infinitamente
    while True:
        print("\n Digite os dados do usuario: ")
        nome = input("Nome: ")
        idade = input("Idade: ")
        email = input("email: ")

        # chamando a função para salvar no arquivo CSV
        salvar_em_csv(nome, idade, email)
        print("Dados salvos com sucesso!")

        continuar = input("Deseja adicionar outro? s/n")
        if continuar != "s":
            break
        
    mostrar_grafico()


if __name__ == "__main__":
    main()
