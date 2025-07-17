import math
import networkx as nx
import matplotlib.pyplot as plt
import scipy

def calcularArbol(datos, numS, listaDatos, listaSigma):
    ultimo_valor = float(datos[-1][1])
    prenultimo_valor = float(datos[-2][1])
    etiquetaS = f"z{numS}"
    valorS = float(ultimo_valor + prenultimo_valor)
    agregarSigma = (etiquetaS, datos[-2][0], datos[-1][0], prenultimo_valor, ultimo_valor)
    listaSigma.append(agregarSigma)
    datos = datos[:-2]
    sigma = (etiquetaS, valorS)
    datos.append(sigma)
    datos.sort(key=clave_ordenamiento)
    numS += 1   
    listaDatos.append(datos)
    if(len(datos)==2):
        return listaDatos, listaSigma
    else:
        return calcularArbol(datos,numS, listaDatos, listaSigma)

def clave_ordenamiento(tupla):
    primer_valor = tupla[1] 
    segundo_valor = tupla[0]  
    # Primer criterio numeros en orden descendente
    if isinstance(primer_valor, int) or isinstance(primer_valor, float):
        criterio_numero = -primer_valor
    else:
        criterio_numero = float('-inf')
    
    # Segundo criterio por caracter
    if isinstance(segundo_valor, str) and len(segundo_valor) == 2:
        criterio_string = segundo_valor
    else:
        criterio_string = ''
    
    return (criterio_numero, criterio_string)

def codificacion(procesos, sigmas, caracteres):
    lista_codificaciones = []
    ramas = []
    for c in caracteres:
        codificacion = 0
        codificacion_completa = []
        rama_completa = []
        rama_completa.append(c)
        caracter = c
        while(codificacion!=2):
            codificacion, caracter = encontrar_caracter(caracter, sigmas)
            if(codificacion!=2):
                codificacion_completa.append(codificacion)
                rama_completa.append(caracter)
        if(caracter == procesos[-1][0][0]):
            codificacion_completa.append(0)
        else:
            codificacion_completa.append(1)
        codificacion_completa.reverse()
        lista_codificaciones.append(codificacion_completa)
        rama_completa.reverse()
        ramas.append(rama_completa)
        print(f"Codificacion de {c}: {codificacion_completa}")
        #print(f"Rama de {c}: {rama_completa}")

    return lista_codificaciones,ramas


def encontrar_caracter(caracter, sigmas):
    codificacion = 2
    for s in sigmas:
            if s[1] == caracter:
                codificacion = 0
                nuevo_caracter = s[0]
                return codificacion, nuevo_caracter
            elif s[2] == caracter:
                codificacion = 1
                nuevo_caracter = s[0]
                return codificacion, nuevo_caracter
            nuevo_caracter = caracter
    return codificacion, nuevo_caracter

def entropia_entre_ramas(sigmas, proceso):
    valores_diferencias = []
    for s in sigmas:
        diferencia = abs(s[3] - s[4])
        if(diferencia>0):
            valores_diferencias.append(diferencia)
    diferencia = abs(proceso [-1][0][1] - proceso [-1][1][1])
    if(diferencia>0):
        valores_diferencias.append(diferencia)
    return valores_diferencias

def calcularEntropia(frec):
    entropia = 0
    for f in frec:
        entropia += -f*math.log2(f)
    return entropia

def calcularRadioCompresion(codificaciones, frecuencias):
    ims = 0
    i=0
    for codificacion in codificaciones:
        ims+= (len(codificacion))*frecuencias[i]
        i+=1
    return 8/ims


print("Arbol de Huffman jerarquico\n")
n = int(input("Ingresa cantidad diferente de caracteres: "))
caracteres = []
frecuencias = []
for i in range(0, n):
    caracter = input(f"Ingrese el caracter {i+1}: ")
    caracteres.append(caracter)
    frecuencia = float(input("Ingresa la frecuencia del caracter: "))
    frecuencias.append(frecuencia)

if sum(frecuencias)==1:
    datos = list(zip(caracteres, frecuencias))
    datos.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)
    listaDatos= []
    listaDatos.append(datos)
    listaSigma = []
    listaProceso, sigmas = calcularArbol(datos, 1, listaDatos, listaSigma)
    print("\nProceso para formar el arbol")
    for fila in listaProceso:
        print(fila)
    print("\nCodificaciones")
    lista_codificaciones, ramas = codificacion(listaProceso,sigmas,caracteres)
    listadiferencias= entropia_entre_ramas(sigmas, listaProceso)
    entropia_ramas = calcularEntropia(listadiferencias)
    entropia_frec = calcularEntropia(frecuencias)
    print(f"\nEntropia de diferencia de ramas: {entropia_ramas} bits/c")
    print(f"Entropia frecuencias: {entropia_frec} bits/c")
    print(f"Entropia total: {entropia_ramas+entropia_frec} bits/c")

    radio_compresion = calcularRadioCompresion(lista_codificaciones, frecuencias)
    print(f"Radio compresion: {radio_compresion}")

    #Graficar
    G = nx.DiGraph()
    nodo_raiz = 'Raiz'
    G.add_edge(nodo_raiz, f'{listaProceso[-1][1][0]}')
    G.add_edge(nodo_raiz, f'{listaProceso[-1][0][0]}')

    # Agregar las ramas al grafo
    for rama in ramas:
        if len(rama) > 1:
            for i in range(len(rama)-1):
                G.add_edge(rama[i], rama[i+1])

    # Dibujar el grafo
    
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
    plt.show()


else:
    print("La suma de las frecuencias de los caracteres deben ser 1")


