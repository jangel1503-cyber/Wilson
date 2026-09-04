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
            # Conversión y cálculo según la nueva especificación
            size_cm = size_in * 2.54            # pulgadas -> centímetros
            mitad = size_cm / 2.0              # dividir entre 2
            dividido = mitad / 100.0           # dividir la mitad entre 100
            cuadrado = dividido ** 2           # elevar al cuadrado
            gramos = cuadrado * 1000.0        # multiplicar por 1000

            st.markdown("**Resultados:**")
            st.write(f"Tamaño ingresado: {size_in:.4g} in")
            st.write(f"Equivalente en cm: {size_cm:.2f} cm")
            st.write(f"Mitad (cm): {mitad:.2f} cm")
            st.write(f"Mitad / 100: {dividido:.4f} cm")
            st.write(f"(Mitad/100)²: {cuadrado:.6f} cm²")
            st.write(f"Resina necesaria: {gramos:.6f} g")

            with st.expander("Ver fórmula utilizada"):
                st.write("Pasos:")
                st.latex(r"\text{cm} = in \times 2.54")
                st.latex(r"\text{mitad} = \frac{\text{cm}}{2}")
                st.latex(r"\text{dividido} = \frac{\text{mitad}}{100}")
                st.latex(r"\text{resultado} = (\text{dividido})^{2} \times 1000")
    except ValueError:
        st.error("Valor no válido — introduce un número en pulgadas.")

st.caption("Archivo: streamlit_app.py — abre con `streamlit run streamlit_app.py` en la carpeta resin-top-calculator.")
