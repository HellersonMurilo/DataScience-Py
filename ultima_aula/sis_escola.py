#ID_Aluno, Nome, Idade, Ano_Serie, Nota

import csv
#path lib para salvar o CSV em uma pasta/caminho
from pathlib import Path

#arquivo do CSV
ARQUIVO = Path('dados_escola.csv')

#Campos dos nossos arquivos
CAMPO = ['ID_Aluno', 'Nome', 'Idade', 'Ano_Serie', 'Nota']

#sistema vai executar ao iniciar
def carregar_arquivo():
    """Carregar o arquivo existente"""
    
    if not ARQUIVO.exists(): #verificando se o arquivo NAO existe
        return [], 1 #lista vazia
    
    #significa que o arquivo existe
    with ARQUIVO.open(newline="", encoding="utf-8") as arquivo:
        
        #leitor, ler o arquivo csv existente
        leitor = csv.DictReader(arquivo)
        
        #capturar os dados, transformar em lista
        dados = list(leitor)
        
    #listaDados, ID
    return dados, len(dados) + 1

def salvar(dados):
    """ Salvar os dados em CSV """
    with ARQUIVO.open("w", newline="", encoding="utf-8") as arquivo:
        #com o arquivo aberto    
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPO)
        
        escritor.writeheader()
        #escrevendo dados no arquivo
        
        escritor.writerows(dados)
        
# criando o sistema
def main():
    dados, proximo_id = carregar_arquivo()
    print('Arquivo: ', ARQUIVO.resolve())
    print('Campos: ',CAMPO)
    
    print('Para parar o sistema, deixe o nome em branco e pressione ENTER')
    
    while True:
        nome = input("Nome: ")
        if nome == "":
            break
        idade = input("Idade: ")
        serie = input("Serie: ")
        nota = input("Nota (0-10): ")
        
        registro = {
            'ID_Aluno': str(proximo_id),
            'Nome': nome,
            'Idade': idade,
            'Ano_Serie': serie,
            'Nota': nota
        }
        
        dados.append(registro)
        proximo_id += 1
        print('Adicionado com sucesso!')
        
    salvar(dados)
    print('Dados salvods com sucesso! em: ', ARQUIVO.resolve())
    
if __name__ == '__main__' :
    main()