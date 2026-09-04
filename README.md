# Calculadora de resina — Tope de mesa

Instrucciones:

- Abre el archivo `index.html` en un navegador web.
- Introduce el tamaño de la mesa en pulgadas (diámetro) y pulsa `Calcular`.

Fórmula usada:

- Radio = mitad del tamaño (pulgadas).
- Área A = π × radio².
- Resultado en gramos = A × 1,000.

- Pasos ahora aplicados en la app:
	1. Convertir pulgadas → cm: `cm = in × 2.54`.
	2. Obtener la mitad: `mitad = cm / 2`.
	3. Dividir la mitad entre 100: `dividido = mitad / 100`.
	4. Elevar al cuadrado: `(dividido)^2`.
	5. Multiplicar por 1000 → gramos.

Ejemplo rápido: para una mesa de 24 pulgadas → cm = 60.96 cm → mitad = 30.48 → dividido = 0.3048 → (dividido)^2 = 0.0929 → resina ≈ 92.90 g.
