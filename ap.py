from plotly.graph_objs._figure import Figure
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise de Dados",layout="wide")

st.title("Análise de Dados de vendas")
st.write("Analise completa de vendas com KPIs, distribuição por estado e canais de venda.")

# -----DADOS FICTÍCIOS PARA O PROJETO-----
dados_vendas = pd.DataFrame({
    "Estado": ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia", "Paraná", "Santa Catarina"],
    "Vendas": [3000, 2500, 1800, 1200, 1500, 1700]
})

Dados_mensal = pd.DataFrame({
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    "Vendas": [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]

})

dados_canais = pd.DataFrame({
    "Canal de Venda": ["E-commerce", "Marketplace", "Loja Física", "Revendedores"],
    "Vendas": [84843, 93500, 76363, 43333]
})

# -----TOP: CARTÕES DE KPIs-----
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Vendas", f"R$ {dados_vendas['Vendas'].sum():,.2f}")
col2.metric("Vendas por Estado", f"R$ {dados_vendas['Vendas'].mean():,.2f}")
col3.metric("Vendas Mensais", f"R$ {Dados_mensal['Vendas'].sum():,.2f}")
col4.metric("Vendas por Canal", f"R$ {dados_canais['Vendas'].sum():,.2f}")

st.divider()

# ----MEIO: GRAFICO -----
col_esq, col_dir = st.columns([1, 1])

with col_esq:
    st.subheader("Venda total por Estado")
    fig_estado=px.bar(
        dados_vendas,
        x="Vendas",
        y="Estado",
        orientation="h",
        text_auto="2s",
        color="Vendas",
        color_continuous_scale="Blues"
    )
    fig_estado.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False)
    st.plotly_chart(fig_estado, use_container_width=True)

    with col_dir:
        st.subheader("Venda total por Mês")
        fig_mes=px.line(
            Dados_mensal,
            x="Mês",
            y="Vendas",
            markers=True,
            line_shape="spline",
        )
        st.plotly_chart(fig_mes, use_container_width=True)

        st.subheader("Venda total por Canal")
        fig_canal: Figure =px.pie(
            dados_canais,
            values="Vendas",
            names="Canal de Venda",
            hole=0.5
        )        
        st.plotly_chart(fig_canal, use_container_width=True)
