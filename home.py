import streamlit as st

st.set_page_config(page_title="Dashboard Lojas", page_icon="🛍️", layout="wide", initial_sidebar_state="collapsed")

st.title("🏠 Home")
st.write("Bem-vindo ao painel de lojas!")

st.markdown("### Acesse as páginas pelas opções abaixo ou pela barra lateral:")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/1_Renner.py", label="Renner", icon="👕")

with col2:
    st.page_link("pages/2_Karsten.py", label="Karsten", icon="👗")

with col3:
    st.page_link("pages/3_Riachuelo.py", label="Riachuelo", icon="🛒")
