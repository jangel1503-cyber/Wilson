import math
import streamlit as st

st.set_page_config(page_title="Calculadora de resina", layout="centered")

st.title("Calculadora de resina — Tope de mesa")
st.write("Introduce el tamaño del tope en pulgadas (diámetro). Deja el campo vacío y escribe el valor.")

# Usamos un campo de texto vacío para que el usuario pueda dejarlo en blanco
size_text = st.text_input("Tamaño (pulgadas)", value="", placeholder="Ej: 24")

if size_text.strip() == "":
    st.info("Escribe el tamaño del tope en pulgadas para calcular la resina.")
else:
    try:
        size_in = float(size_text)
        if size_in <= 0:
            st.error("Introduce un número mayor que 0.")
        else:
            # Secuencia: dividir entre 2, dividir entre 100, elevar al cuadrado,
            # multiplicar por 3.1416 y luego por 1000
            mitad = size_in / 2.0
            dividido = mitad / 100.0
            cuadrado = dividido * dividido
            por_pi = cuadrado * 3.1416
            gramos = por_pi * 1000.0

            st.markdown("**Resultados:**")
            st.write(f"Tamaño ingresado: {size_in:.6f}")
            st.write(f"Mitad: {mitad:.6f}")
            st.write(f"Mitad / 100: {dividido:.6f}")
            st.write(f"(Mitad/100)²: {cuadrado:.9f}")
            st.write(f"× 3.1416: {por_pi:.9f}")
            st.write(f"Resina necesaria: {gramos:.6f} g")

            with st.expander("Ver fórmula utilizada"):
                st.write("Pasos ejecutados:")
                st.latex(r"\text{mitad} = \frac{\text{tamaño}}{2}")
                st.latex(r"\text{dividido} = \frac{\text{mitad}}{100}")
                st.latex(r"\text{resultado} = (\text{dividido})^{2} \times 3.1416 \times 1000")
    except ValueError:
        st.error("Valor no válido — introduce un número en pulgadas.")

st.caption("Archivo: streamlit_app.py — abre con `streamlit run streamlit_app.py` en la carpeta resin-top-calculator.")
