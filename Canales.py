import csv 
import math

def leer_csv(file_path):
    datos = []
    pi = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        for row in reader:
            datos.append(row[2:]) 
            pi.append(row[0])  
    return datos, pi

def frecuencia_entrada(datos):
    frecuencias_entrada = []
    for fila in datos:
        suma = 0
        for f in fila:
            valor = float(f)
            suma+=valor
        frecuencias_entrada.append(suma)
    return frecuencias_entrada

def frecuencias_salida(datos):
    frecuencias_salida = []
    suma_producto = []
    for i in range(len(datos[0])):
        suma = 0
        for j in range(len(datos)):
            valor = float(datos[j][i]) 
            suma += valor 
        frecuencias_salida.append(suma) 
    return frecuencias_salida


def matriz_transmision(datos, pi):
    w=0
    datos_matriz = []
    for fila in datos:
        valores = []
        for f in fila:
            valor = float(f)
            pi_valor = float(pi[w])
            nuevo_valor = valor*pi_valor
            valores.append(nuevo_valor)
        datos_matriz.append(valores)
        w+=1
    return datos_matriz

def sumaproductoColumnas(datos, pi):
    suma_producto = []
    for i in range(len(datos[0])):
        suma = 0
        for j in range(len(datos)):
            valor = float(datos[j][i]) 
            pi_actual = float(pi[i])
            multi = valor  * pi_actual
            suma +=multi
        suma_producto.append(suma) 
    return suma_producto

def funcionSumatoria(datos, sumaproducto):
    nueva_matriz = []
    for fila in datos:
        h=0
        fil = []
        for p in fila:
            valor = float(p)
            sumaprod = sumaproducto[h]
            nuevo_valor = valor * math.log2(valor / sumaprod)
            fil.append(nuevo_valor)
            h+=1
        nueva_matriz.append(fil)

    return nueva_matriz
   
def obtenerInformacionPorAlfabeto(datos, pi):
    cantidad_lista = []
    cantidad_total = 0
    for fila in datos:
        i = 0
        suma = 0
        for p in fila:
            valor = float(p)
            suma+=valor
        pi_actual = float(pi[i])
        cant = pi_actual*suma
        cantidad_lista.append(cant)
        cantidad_total += (pi_actual*suma)
        i+=1

    return cantidad_lista, cantidad_total
def imprimir(datos):
    for fila in datos:
        for f in fila:
            print(f,end=" - ")
        print()

def imprimir2(datos):
    for valor in datos:
        print(valor, end=" - ")

            
#Leer la matriz de transicion del archivo csv 

archivo = "matriz_probabilidades.csv"
datos, pi = leer_csv(archivo)

#La pasamos a matriz de transmision total 
datos_finales = matriz_transmision(datos,pi)
print("Matriz de transmicion total")
imprimir(datos_finales)

#Calculamos las frecuencias de entrada y salida
frec_entrada = frecuencia_entrada(datos_finales)
frec_salida = frecuencias_salida(datos_finales)
print("\n")
print("Frecuencias de entrada")
print(frec_entrada)
print()
print("Frecuencias de salida")
print(frec_salida)

sumaproducto = sumaproductoColumnas(datos, pi)
#print(sumaproducto)

#Calculamos I(A,B)
nueva_matriz = funcionSumatoria(datos,sumaproducto)
print("\nMatriz I(A, B)")
imprimir(nueva_matriz)
#print(nueva_matriz)

#Obtenemos la cantidad de informacion por alfabeto enviado 
cant, cant_total = obtenerInformacionPorAlfabeto(nueva_matriz,pi)

print(f"\nCantidad de información por cada alfabeto enviado: +{cant_total} bits/sim")



