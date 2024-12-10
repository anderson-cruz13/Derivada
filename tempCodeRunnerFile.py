while calculo < relative_error_direito or calculo > relative_error_esquerdo:
    point_x += 1
    calculo = derivada.subs(x, point_x)
    print(calculo, point_x)
    input()