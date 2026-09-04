# Calculadora de resina — Tope de mesa

Instrucciones:

- Abre el archivo `index.html` en un navegador web.
- Introduce el tamaño de la mesa en pulgadas (diámetro) y pulsa `Calcular`.

Fórmula usada (secuencia exacta aplicada):

1. Convertir pulgadas → cm: `cm = in × 2.54`.
2. Dividir entre 2: `mitad = cm / 2`.
3. Dividir la mitad entre 100: `dividido = mitad / 100`.
4. Multiplicar por sí mismo (elevar al cuadrado): `cuadrado = dividido * dividido`.
5. Multiplicar por π aproximado: `por_pi = cuadrado * 3.1416`.
6. Multiplicar por 1000 → `gramos = por_pi * 1000`.

Ejemplo rápido: para una mesa de 24 pulgadas → cm = 60.96 → mitad = 30.48 → dividido = 0.3048 → (dividido)^2 = 0.0929 → ×3.1416 = 0.2917 → resina ≈ 291.7 g.
