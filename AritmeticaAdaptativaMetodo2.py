import csv
from itertools import product

def ingresar_caracteres():
    cantidad_caracteres = int(input("Ingresa la cantidad de caracteres diferentes: "))
    caracteres = {}
    for i in range(cantidad_caracteres):
        caracter = input(f"Ingresa el caracter {i + 1}: ")
        frecuencia = float(input(f"Ingresa la frecuencia del caracter {caracter}: "))
        caracteres[caracter] = frecuencia
    return caracteres

def generar_combinaciones(cadena, espacios):
    combinaciones = [''.join(p) for p in product(cadena, repeat=espacios)]
    return combinaciones

def adaptative_arithmetic_coding(alfa_original, beta_original):
    alfa, codificacion_alfa = binary_expansion(alfa_original)
    beta, codificacion_beta = binary_expansion(beta_original)
    codificacion = []
    alfa_actual = alfa
    while codificacion_alfa == codificacion_beta:
        alfa, codificacion_alfa = binary_expansion(alfa)
        beta, codificacion_beta = binary_expansion(beta)
        if codificacion_alfa == codificacion_beta:
            codificacion.append(codificacion_alfa)    
            alfa_actual = alfa
    if codificacion_alfa == 1:
        alfa_anterior = alfa 
        alfa, codificacion_alfa = binary_expansion(alfa)
        if alfa_anterior == alfa:
            codificacion.append(codificacion_alfa)
    else:
        existe_uno = False
        alfa_ac = alfa
        while alfa > 0 and not existe_uno:
            alfa, codificacion_alfa = binary_expansion(alfa)
            if codificacion_alfa == 1:
                existe_uno = True
        if existe_uno:
            a, c = binary_expansion(alfa_actual)
            codificacion.append(c)
            alfa, codificacion_alfa = binary_expansion(alfa_ac)
            codificacion.append(codificacion_alfa)
            while codificacion_alfa == 0:
                alfa, codificacion_alfa = binary_expansion(alfa_actual)
                if codificacion != 0:
                    codificacion.append(codificacion_alfa)
            codificacion.append(1)
        if len(codificacion) == 0:
            alfa, codificacion_alfa = binary_expansion(alfa_original)
            codificacion.append(codificacion_alfa)
    return codificacion

def binary_expansion(r):
    if r >= 1:
        codificacion = 1
        r = (r - 1) * 2
    else:
        codificacion = 0
        r *= 2
    return r, codificacion

caracteres = ingresar_caracteres()
claves = caracteres.keys()
string_caracteres = ''.join(claves)
if sum(caracteres.values()) == 1:
    datos = []
    print("Generando codificaciones....")
    for i in range(1, len(string_caracteres) + 1):
        combinaciones_nivel = generar_combinaciones(string_caracteres, i)
        beta = 0
        alfa = 0
        valores_combinacion = []
        for combinacion in combinaciones_nivel:
            l = 1
            for c in combinacion:
                l *= caracteres[c]
            alfa = beta 
            beta = alfa + l
            codificacion = adaptative_arithmetic_coding(alfa, beta)
            com = [(combinacion, l, alfa, beta, codificacion)]
            valores_combinacion.append(com)
        nivel = [(i, valores_combinacion)]
        datos.append(nivel)
    print("Generando archivo csv....")
    try:
        with open('AritmeticaAdaptativaMetodo2.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for dato in datos:  
                writer.writerow(['', 'Longitud', 'Alfa', 'Beta', 'Codificacion'])
                writer.writerow([f"Nivel {dato[0][0]}", "", "", "", ""])
                for c in dato[0][1]:
                    writer.writerow([c[0][0], c[0][1], c[0][2], c[0][3], c[0][4]])
                writer.writerow([''])
        print("Archivo generado con éxito")
    except Exception as e:
        print("Error al generar archivo csv")
else:
    print("La suma de las frecuencias debe ser 1")
