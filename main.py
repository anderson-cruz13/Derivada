import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, solve  # type: ignore
from typing import Any


x: Any = symbols("x")
equacao: Any = x**2 + 2
equacao_resolvida: Any = solve(equacao, x)
derivada: Any = diff(equacao, x)

a: float = 3.0
b: float = 2.0
yA: float = equacao.subs(x, a)
yB: float = equacao.subs(x, b)

taxa_media: float = (yB - yA) / (b - a)

relativo_erro_direito: float = taxa_media - (taxa_media * 0.01)
relativo_erro_esquerdo: float = taxa_media + (taxa_media * 0.01)

calculo: float = 0.0
point_x: float = 0.0

while not (relativo_erro_direito <= calculo <= relativo_erro_esquerdo):
    point_x += 0.1
    calculo = derivada.subs(x, point_x)
    if abs(calculo - taxa_media) < 0.01:
        break

# Definindo os pontos para plotagem
x_vals = np.linspace(a - 1, b + 1, 500)
y_vals = [float(equacao.subs(x, val)) for val in x_vals]
point_y = float(equacao.subs(x, point_x))

# Plotagem
plt.figure(figsize=(10, 6))

# Gráfico da equação
plt.plot(x_vals, y_vals, label="Equação $f(x) = x^2 + 2$", color="blue")

# Segmento no intervalo [a, b]
plt.plot(
        [a, b], [yA, yB], label="Segmento [$a, b$]", color="green",
        linestyle="--")

# Tangente no ponto c
tangent_slope = float(derivada.subs(x, point_x))
tangent_y = tangent_slope * (x_vals - point_x) + point_y
plt.plot(
        x_vals, tangent_y, label=f"Tangente no ponto $c={point_x:.2f}$",
        color="red", linestyle=":")

# Destaques para os pontos
plt.scatter([a, b, point_x], [yA, yB, point_y], color="black", zorder=5)
plt.text(a, yA, f"A({a:.1f}, {yA:.1f})", fontsize=9)
plt.text(b, yB, f"B({b:.1f}, {yB:.1f})", fontsize=9)
plt.text(point_x, point_y, f"C({point_x:.1f}, {point_y:.1f})", fontsize=9)

# Configurações do gráfico
plt.title("Gráfico da Equação, Segmento [$a, b$] e Tangente no Ponto $c$")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.grid(alpha=0.3)
plt.legend()
plt.show()
