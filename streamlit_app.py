import math
import streamlit as st

st.set_page_config(page_title="Calculadora de resina", layout="centered")

st.title("Calculadora de resina — Tope de mesa")
st.write("Introduce el tamaño de la mesa en pulgadas (diámetro). Se calcula el área del círculo y se multiplica por 1,000 para obtener gramos.")

size = st.number_input("Tamaño (pulgadas, diámetro)", min_value=0.0, value=24.0, step=0.1, format="%.2f")

if size <= 0:
    st.warning("Introduce un tamaño mayor que 0")
else:
    radio = size / 2.0
    area = math.pi * radio ** 2  # A = π * r^2
    gramos = area * 1000.0

    st.markdown("**Resultados:**")
    st.write(f"Radio: {radio:.2f} in")
    st.write(f"Área: {area:.2f} in²")
    st.write(f"Resina necesaria: {gramos:.2f} g")

    with st.expander("Ver fórmula utilizada"):
        st.latex(r"A = \\pi \times r^{2}")
        st.write("Radio = mitad del tamaño (diámetro). Resultado final = A × 1000 (g).")

st.caption("Archivo: streamlit_app.py — abre con `streamlit run streamlit_app.py` en la carpeta `resin-top-calculator`.")
