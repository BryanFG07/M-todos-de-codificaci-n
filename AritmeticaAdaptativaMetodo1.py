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

def adaptative_arithmetic_coding(l, alfa, beta):
    t = 1
    t_calculo = 0.5 ** t
    while t_calculo > l:
        t += 1
        t_calculo = 0.5 ** t
    dos_t = 2 ** -t
    dos_menos_t = 2 ** (-t + 1)
    if dos_t <= l < dos_menos_t:
        desigualdad_menor = alfa * (2 ** t)
        desigualdad_mayor = beta * (2 ** t)
        x = desigualdad_menor if desigualdad_menor % 2 == 0 else desigualdad_mayor
        codificacion = binary_expansion(x, t)  
    elif dos_t <= l:
        x = alfa * (2 ** t)
        codificacion = binary_expansion(x, t)  
    elif l < dos_menos_t:
        x = beta * (2 ** t)
        codificacion = binary_expansion(x, t)  
    else: 
        codificacion = "Error"
    return codificacion

def binary_expansion(x, t):
    r = x / (2 ** t)
    codificacion = "["
    while r != 0:
        r *= 2
        if r >= 1:
            codificacion += "1"
            r -= 1
        else:
            codificacion += "0"
    codificacion += "]"
    return codificacion
    
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
            codificacion = adaptative_arithmetic_coding(l, alfa, beta)
            com = [(combinacion, l, alfa, beta, codificacion)]
            valores_combinacion.append(com)
        nivel = [(i, valores_combinacion)]
        datos.append(nivel)
    print("Generando archivo csv....")
    try:
        with open('AritmeticaAdaptativa.csv', mode='w', newline='', encoding='utf-8') as file:
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
