from typing import Callable as Callab
import matplotlib.pyplot as plt
import numpy as np


def f(x: float) -> float:
    return x ** 2 + 2


def f_derivada(
        f: Callab[[float], float],
        x: float) -> float:

    h: float = 1e-6
    return (f(x + h) - f(x)) / h


def tangente_f(
        f: Callab[[float], float],
        a: float, b: float,
        taxa: float,
        tolerancia: float = 1e-3) -> float | None:

    h: float = 1e-6
    passo = h if b > a else -h
    c: float = a + passo
    derivada = f_derivada(f, c)

    while derivada < taxa:
        c = c + passo
        derivada = f_derivada(f, c)

    return c


a: float = -2
b: float = 2

try:
    taxa: float = (f(b) - f(a)) / (b - a)
except ZeroDivisionError:
    print('Divisão por zero')
    exit(1)

c: float | None = tangente_f(f, a, b, taxa)

if __name__ == '__main__':
    plt.axvline(0, color='black', linestyle='--')
    plt.axhline(0, color='black', linestyle='--')
    plt.grid(True)

    x = np.linspace(a - 2, b + 2, 100)
    y = f(x)  # type: ignore
    plt.plot(x, y, label='Função f(x)', color='blue')

    secante_y = f(a) + taxa * (x - a)
    plt.plot(x, secante_y, label='Secante (Taxa)', color='red', linestyle='--')

    plt.scatter(a, f(a), color='green', label='Ponto A')
    plt.scatter(b, f(b), color='red', label='Ponto B')

    if c is not None:
        plt.scatter(c, f(c), color='orange', label='Ponto C')
        tangente_y = f(c) + f_derivada(f, c) * (x - c)
        plt.plot(x, tangente_y, label='Tangente', color='green', linestyle=':')

    plt.legend()
    plt.show()
