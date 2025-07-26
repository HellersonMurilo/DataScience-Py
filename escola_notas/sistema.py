import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Escolar", layout="wide")
st.title("Dashboard de Desempenho Escolar")

# upload de arquivo
arquivo = st.file_uploader("Envie o arquivo CSV com notas", type=["csv"])

if arquivo:
    try:
        # lendo o arquivo csv
        df = pd.read_csv(arquivo)

        # capturando as datas
        df["Data_Prova"] = pd.to_datetime(df["Data_Prova"])
        df["Mes"] = df["Data_Prova"].dt.to_period("M").astype(str)

        # KPI - Indicador Chave de desempenho
        media_geral = df["Nota"].mean()
        disciplina = df.groupby("Disciplina")["Nota"].mean().idxmax()
        aluno_pior = df.groupby("Aluno")["Nota"].mean().idxmin()

        # Coluna
        col1, col2, col3 = st.columns(3)
        col1.metric("Média Geral", f"{media_geral:.2f}")
        col2.metric("Melhor Disciplina", disciplina)
        col3.metric("Aluno com a menor média", aluno_pior)

        # Filtros
        aluno_sel = st.selectbox("Filtrar por Aluno:", df["Aluno"].unique())
        df_filtrado = df[df["Aluno"] == aluno_sel]

        # Título do gráfico
        st.subheader(f"Notas de {aluno_sel} por disciplina")

        # Gráfico de barras
        fig_bar = px.bar(
            df_filtrado, x="Disciplina", y="Nota", color="Disciplina", text_auto=True
        )
        st.plotly_chart(fig_bar, use_container_width=True)

        # Gráfico de linha - evolução das notas por mês
        st.subheader("Evolução de Notas por Mês")
        fig_linha = px.line(
            df,
            x="Mes",
            y="Nota",
            color="Aluno",
            markers=True,
            title="Notas ao longo do tempo",
        )
        st.plotly_chart(fig_linha, use_container_width=True)

    except Exception as e:
        st.error(f"🚨 Erro ao processar o arquivo: {e}")  # <-- CORRETO
else:
    st.info("Envie um arquivo CSV com as colunas: Aluno, Disciplina, Data_Prova, Nota")
