import math

def calcularEntropia(frec):
    entropia = -frec * math.log2(frec)
    return entropia

def calcularRadioCompresion(codificaciones, frecuencias):
    ims = 0
    i = 0
    for codificacion in codificaciones:
        ims += (len(codificacion)) * frecuencias[i]
        i += 1
    return 8 / ims

def generar(simbolos, probabilidades):
    nodos = list(zip(simbolos, probabilidades))
    nodos.sort(key=lambda x: x[1], reverse=True)

    while len(nodos) > 1:
        nuevo_nodo = (None, nodos[-1][1] + nodos[-2][1])
        nodos.append((nodos.pop(-1)[0], nuevo_nodo[1]))
        nodos.pop(-2)
        nodos.sort(key=lambda x: x[1], reverse=True)

    return nodos[0]

def generar_codigos(arbol, codigo="", codigos={}):
    if isinstance(arbol[0], str):
        codigos[arbol[0]] = codigo
    else:
        generar_codigos(arbol[0], codigo + "0", codigos)
        generar_codigos(arbol[1], codigo + "1", codigos)
    return codigos

# Método de Shannon-Fano
print("Método de Shannon-Fano\n")
n = int(input("Ingresa la cantidad de caracteres diferentes: "))
caracteres = []
frecuencias = []
for i in range(n):
    caracter = input(f"Ingrese el caracter {i+1}: ")
    caracteres.append(caracter)
    frecuencia = float(input("Ingresa la frecuencia del caracter: "))
    frecuencias.append(frecuencia)

if sum(frecuencias) == 1:
    arbol = generar(caracteres, frecuencias)
    codigos = generar_codigos(arbol)

    entropia = sum(calcularEntropia(frec) for frec in frecuencias)
    print(f"Entropia: {entropia} bits/c ")

    print("Codificaciones:")
    for caracter, codificacion in codigos.items():
        print(f"{caracter}: {codificacion}")

    #radio = calcularRadioCompresion(codigos.values(), frecuencias)
    #print(f"Radio de compresión: {radio}")
else:
    print("La suma de las frecuencias debe ser 1")
