primer mes 💖
import streamlit as st
import time

st.set_page_config(page_title="Feliz primer mes ❤️", layout="centered")

# Estilos
st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 55px;
    color: #e60073;
    font-weight: bold;
}
.msg {
    text-align: center;
    font-size: 26px;
    color: #ff3399;
}
</style>
""", unsafe_allow_html=True)

# Título
st.markdown(
    '<div class="title">💖 Feliz primer mes, mi niño hermoso 💖</div>',
    unsafe_allow_html=True
)

st.write("")

# Mensajes que aparecen poco a poco
messages = [
    "Desde que llegaste a mi vida todo es más bonito 💕",
    "Gracias por cada momento, cada risa y cada abrazo 🥰",
    "Este primer mes ha sido muy especial para mí ✨",
    "Y quiero preguntarte algo muy importante… 💌"
]

placeholder = st.empty()

for msg in messages:
    placeholder.markdown(
        f'<div class="msg">{msg}</div>',
        unsafe_allow_html=True
    )
    time.sleep(2)

st.write("")
st.write("")

# Pregunta final
st.markdown(
    '<div class="msg"><b>¿Quieres seguir siendo mi novio? 💖</b></div>',
    unsafe_allow_html=True
)

st.write("")

col1, col2 = st.columns(2)

with col1:
    if st.button("💗 SÍ 💗"):
        st.balloons()
        st.success("Sabía que dirías que sí 😍💞 Te quiero muchísimo ❤️")

with col2:
    if st.button("💔 NO"):
        st.warning("Esa opción solo era de adorno 😌💗 Intenta otra vez")
