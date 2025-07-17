from itertools import product

def combinaciones(posicion, conjunto):
    return list(product(conjunto, repeat=posicion)) if posicion >= len(next(iter(conjunto))) else []

A = {'0000', '1111'}
B = {'0000', '1111', '****'}

for posicion in range(1, 6):  # Ajustado para manejar posiciones hasta 20
    combinaciones_A = combinaciones(posicion, A)
    combinaciones_B = combinaciones(posicion, B)
    if not combinaciones_A:
        print(f'Error: No se pueden generar combinaciones de longitud {posicion} en A')
    else:
        print(f'Posición {posicion} en A: {len(combinaciones_A)} combinaciones')
        print(combinaciones_A)
    if not combinaciones_B:
        print(f'Error: No se pueden generar combinaciones de longitud {posicion} en B')
    else:
        print(f'Posición {posicion} en B: {len(combinaciones_B)} combinaciones')
        print(combinaciones_B)
