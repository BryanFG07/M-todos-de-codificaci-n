import math
def calcularFi(frecuencias):
    fi_anterior = 0 
    FI = []
    suma = 0
    for i in range(0, len(frecuencias)):
        frec_actual = suma + (float(frecuencias[i]) / 2)
        suma += float(frecuencias[i])
        FI.append(frec_actual)
        i+=1
    return FI

def calcularLK(FI):
    LK = []
    for f in FI:
        f_actual = float(f)
        lk = math.log((1/f_actual), 2)
        lk_redondeado = math.ceil(lk) 
        LK.append(lk_redondeado)
    return LK

def expansionBinaria(FI,LK):
    R_actual = FI*2
    codificacion = ""
    for i in range(LK):
        if R_actual>=1:
            codificacion = codificacion + "1"
            R_actual = (R_actual - 1) * 2
        else:
            codificacion = codificacion + "0"
            R_actual = R_actual * 2

    return codificacion

def calcularEntropia(frec):
    entropia = -frec*math.log2(frec)
    return entropia

def calcularRadioCompresion(codificaciones, frecuencias):
    ims = 0
    i=0
    for codificacion in codificaciones:
        ims+= (len(codificacion))*frecuencias[i]
        i+=1
    return 8/ims

print("Metodo de Shannon Fannon Elias\n")
n = int(input("Ingresa cantidad diferente de caracteres: "))
caracteres = []
frecuencias = []
for i in range(0, n):
    caracter = input(f"Ingrese el caracter {i+1}: ")
    caracteres.append(caracter)
    frecuencia = float(input("Ingresa la frecuencia del caracter: "))
    frecuencias.append(frecuencia)
combinado = list(zip(caracteres, frecuencias))
#Ordenamos por frecuencia y por segundo criterio por orden alfabetico
ordenados_com= sorted(combinado, key=lambda x: (x[1], x[0]))

caracteres_ordenados, frecuencias_ordenados = zip(*ordenados_com)

if sum(frecuencias)==1:
    FI_list = calcularFi(frecuencias_ordenados)
    LK_list = calcularLK(frecuencias_ordenados)
    print("Codificaciones ")

    entropia = sum(calcularEntropia(frec) for frec in frecuencias_ordenados)
    codificaciones = []
    for f in range(0, len(frecuencias_ordenados)):
        codificion = expansionBinaria(FI_list[f],LK_list[f])
        print(f"{caracteres_ordenados[f]}: {codificion}")
        codificaciones.append(codificion)
    print(f"Entropia: {entropia} bits/c ")
    radio = calcularRadioCompresion(codificaciones, frecuencias_ordenados)
    print(f"Radio de compresion: {radio}")
else:
    print("La suma de las frecuencias debe de ser 1")