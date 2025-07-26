import pandas as pd
import matplotlib.pyplot as plt

# ler o CSV
df = pd.read_csv("aula 4/vendas_loja.csv")

# nomes das colunas
# criar coluna chamada receita
df["Receita"] = df["Quantidade"] * df["Preco_Unitario"]

# sum -> somar
total_receita = df["Receita"].sum()

print(f'total de vendas R${total_receita}')

# mean -> media
media_receita = df['Receita'].mean()
print(f"Média da Receita: R${round(media_receita, 2)}")

# produto mais vendido em quantidade
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()

# idmax -> pegar o maior valor
print('Produto mais vendido: ', produto_mais_vendido)

#grafico de barras - Receita por categoria
df.groupby("Categoria")["Receita"].sum().plot(kind="bar", title="Receita por Categoria")
plt.ylabel("Receita (R$)")
plt.tight_layout() #finalizar o layout
plt.show()

#Grafico de linha - Receita por mes
#Datetime
df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.to_period("M") #Capturando o M - Mes data
#group by
df.groupby("Mes")["Receita"].sum().plot(kind="line", title="Receita Mensal")
plt.ylabel("Receita R$")
plt.xlabel("Mes")
plt.tight_layout()
plt.show()