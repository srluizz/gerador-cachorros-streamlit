import streamlit as st 
import requests 

url = "https://dog.ceo/api/breeds/image/random"


#Titulo da página
st.markdown("<h1 style='text-align: center'>Gerador Aleatório de Imagens de Cachorros</h1>", unsafe_allow_html=True)

### Colunas ###
col1, col2, col3 = st.columns(3)

### Botão Novo Cachorro ###
with col2:
    if st.button("🐶 Novo Cachorro 🐶"):
        st.rerun()
    
dados = requests.get(url).json()

with col2:
    st.image(dados['message'])
    

#Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray; font-size: 14px;'>
        Desenvolvido por <b>Luiz Roberto</b> 🐾 | Dados da API: <a href='https://dog.ceo/dog-api/' target='_blank'>Dog CEO</a> | <a href="
https://github.com/srluizz/gerador-cachorros-streamlit">GitHub</a>
    </p>
    """,
    unsafe_allow_html=True
)




