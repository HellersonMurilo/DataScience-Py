import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações iniciais
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
sns.set_style("whitegrid")

# Carregar dados
df = pd.read_csv("aula 4/vendas_loja.csv")
df["Receita"] = df["Quantidade"] * df["Preco_Unitario"]
df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.to_period("M").astype(str)

# Título
st.title("📊 Dashboard de Vendas")

# KPIs principais
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Total de Vendas", f"R$ {df['Receita'].sum():,.2f}")
with col2:
    st.metric("📦 Total de Produtos Vendidos", int(df["Quantidade"].sum()))
with col3:
    st.metric("📈 Receita Média por Venda", f"R$ {df['Receita'].mean():,.2f}")

st.markdown("---")

# Filtro de categoria
st.sidebar.header("🎯 Filtros")
categorias = df["Categoria"].unique()
categoria_selecionada = st.sidebar.selectbox("Selecione uma categoria:", categorias)

df_filtrado = df[df["Categoria"] == categoria_selecionada]

# Gráfico 1: Receita por Produto (Barra)
st.subheader(f"🔍 Receita por Produto ({categoria_selecionada})")
fig1, ax1 = plt.subplots(figsize=(10, 5))
df_filtrado.groupby("Produto")["Receita"].sum().sort_values().plot(
    kind="barh", color="#4c72b0", ax=ax1
)
ax1.set_xlabel("Receita (R$)")
ax1.set_ylabel("Produto")
ax1.set_title("Receita por Produto")
st.pyplot(fig1)

# Gráfico 2: Receita Mensal (Linha)
st.subheader("📅 Receita Mensal")
fig2, ax2 = plt.subplots(figsize=(10, 5))
df.groupby("Mes")["Receita"].sum().plot(marker="o", color="#55a868", ax=ax2)
ax2.set_xlabel("Mês")
ax2.set_ylabel("Receita (R$)")
ax2.set_title("Evolução da Receita Mensal")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Gráfico 3: Participação por Categoria (Pizza)
st.subheader("🧩 Participação por Categoria")
fig3, ax3 = plt.subplots(figsize=(6, 6))
df.groupby("Categoria")["Receita"].sum().plot(
    kind="pie", autopct="%1.1f%%", startangle=90, ax=ax3, cmap="tab20"
)
ax3.set_ylabel("")
ax3.set_title("Distribuição de Receita por Categoria")
st.pyplot(fig3)
