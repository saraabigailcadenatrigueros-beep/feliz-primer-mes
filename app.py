import streamlit as st
import time
import random

st.set_page_config(
    page_title="Feliz primer mes ❤️",
    layout="centered"
)

# 💅 Estilos adaptados a celular
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #fff0f5, #ffe6f0);
}
.title {
    text-align: center;
    font-size: 42px;
    color: #e60073;
    font-weight: bold;
    margin-bottom: 20px;
}
.msg {
    text-align: center;
    font-size: 22px;
    color: #ff3385;
    margin: 15px 0;
}
.heart {
    font-size: 30px;
    animation: float 2s ease-in-out infinite;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}
.button > button {
    width: 100%;
    font-size: 20px;
    border-radius: 25px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# 💖 Título
st.markdown(
    '<div class="title">💖 Feliz primer mes, mi niño hermoso 💖</div>',
    unsafe_allow_html=True
)

# 💕 Corazones flotando
hearts = " ".join(random.choice(["💖","💗","💘","💞","💕"]) for _ in range(7))
st.markdown(f'<div style="text-align:center" class="heart">{hearts}</div>', unsafe_allow_html=True)

st.write("")

# ⏳ Mensajes progresivos
messages = [
    "Desde que llegaste a mi vida todo es más bonito 💕",
    "Tu sonrisa se volvió una de mis cosas favoritas 🥰",
    "Gracias por cada risa, cada abrazo y cada momento juntos ✨",
    "Este primer mes ha sido muy especial para mí 💞",
    "Y apenas es el comienzo… 💌",
    "Porque contigo quiero muchos meses más ❤️"
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

# 💌 Pregunta final
st.markdown(
    '<div class="msg"><b>¿Quieres seguir siendo mi novio? 💖</b></div>',
    unsafe_allow_html=True
)

st.write("")

col1, col2 = st.columns(2)

with col1:
    if st.button("💗 SÍ, OBVIO 💗"):
        st.balloons()
        st.success("Sabía que dirías que sí 😍💞 Gracias por hacerme tan feliz ❤️")
        st.markdown(
            '<div class="msg">Te quiero hoy, mañana y siempre 💖</div>',
            unsafe_allow_html=True
        )

with col2:
    if st.button("💔 NO"):
        st.warning("Esa opción solo estaba de broma 😌💗 Intenta otra vez")
