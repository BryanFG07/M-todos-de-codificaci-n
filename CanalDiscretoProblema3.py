import csv
from itertools import product

def generar_combinacionesA(A, l):
    combinaciones_A = [''.join(p) for p in product(A, repeat=l)]
    return combinaciones_A

def generar_combinacionesB(B, l):
    combinaciones_B = []
    for p in product(B, repeat=l):
        combinacion = ''.join(p)
        if len(combinacion) == l:
            combinaciones_B.append(combinacion)
    for i in B:
        if len(i) == l:
            if i is not combinaciones_B:
                combinaciones_B.append(i)
    return combinaciones_B



A = {'!', '#', '$', '%', '&'}
B = {'!', '##', '$$', '%%%', '&&&&'}

with open('Problema3_canal_discreto.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir la cabecera del CSV
    writer.writerow([ 'Combinaciones A', 'Numero de A', 'Combinaciones B', 'Numero de B'])
    for l in range(1, 6): #aqui se especifica cuantas iteraciones
        combinaciones_A = generar_combinacionesA(A, l)
        combinaciones_B = generar_combinacionesB(B, l)
        print(f"Para l={l}:")
        print("Combinaciones de A:", combinaciones_A)
        print("nA ="+   str(len(combinaciones_A)))
        print("Combinaciones de B:", combinaciones_B)
        print("nB ="+   str(len(combinaciones_B)))
        writer.writerow([combinaciones_A, len(combinaciones_A), combinaciones_B, len(combinaciones_B)])
