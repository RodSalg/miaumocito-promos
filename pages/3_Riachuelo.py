import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(
    page_title="Riachuelo", 
    page_icon="🛒", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.title("🛒 Loja Riachuelo")
st.write("Veja abaixo os produtos miaumocita:")

urls = [
    "https://www.riachuelo.com.br/jogo-de-cama-bordado-rosaria-floral-branco-casa-riachuelo-15660672001_sku_sku_casal_branco?sku=15770427001",
    "https://www.riachuelo.com.br/kit-colcha-casal-3-pecas-soft-touch-pontos-cruzados-rosa-casa-riachuelo-15846962001_sku_sku?sku=15770427001"
]

produtos = []

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        titulo = soup.title.text if soup.title else "Sem título"
        titulo = titulo.replace("Riachuelo | ", "").strip()

        match = re.search(r'"listPrice":([\d\.]+),"salePrice":([\d\.]+),"soldOut":(true|false)', html)

        if match:
            list_price = float(match.group(1))
            sale_price = float(match.group(2))
            sold_out = match.group(3) == "true"
            promocao = sale_price < list_price

            produtos.append({
                "Produto": titulo,
                "Original": list_price,
                "Promoção": sale_price,
                "Promo?": promocao
            })
    except Exception as e:
        produtos.append({
            "Produto": f"Erro ao acessar: {url}",
            "Original": None,
            "Promoção": None,
            "Promo?": False
        })

# Exibir em cards (mais amigável no celular)
st.markdown("### 🧾 Produtos Monitorados")

for p in produtos:
    with st.container():
        st.markdown(f"### {p['Produto']}")

        if p["Original"] and p["Promoção"]:
            st.markdown(
                f"""
                |💰 Valor Normal:| R$ {p['Original']:.2f}  
                |🔖 Valor Promocional:| R$ {p['Promoção']:.2f}  
                |📉 Está em promoção?| {"✅ Sim" if p['Promo?'] else "❌ Não"}
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("Não foi possível obter os preços.")

    st.divider()
