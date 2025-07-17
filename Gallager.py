import csv
import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Clase Nodo
class Nodo:
    def __init__(self, caracter=None, peso=0):
        self.caracter = caracter
        self.peso = peso
        self.izquierdo = None
        self.derecho = None
        self.padre = None

    # Método para comparar nodos
    def __lt__(self, otro):
        return self.peso < otro.peso

# Función para incrementar el peso según el método de Gallager
def incrementar_peso(nodo):
    nodo.peso += 1
    while nodo.padre:
        padre = nodo.padre
        if nodo == padre.izquierdo:
            hermano = padre.derecho
        else:
            hermano = padre.izquierdo
        
        if nodo.peso > hermano.peso:
            # Intercambiar nodos
            if nodo == padre.izquierdo:
                padre.izquierdo, padre.derecho = padre.derecho, padre.izquierdo
            else:
                padre.derecho, padre.izquierdo = padre.izquierdo, padre.derecho
            
            nodo, hermano = hermano, nodo
        
        nodo = nodo.padre
        nodo.peso += 1

# Función para construir el árbol de Huffman inicial
def construir_arbol_huffman(frecuencias):
    heap = [Nodo(caracter, peso) for caracter, peso in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        izquierdo = heapq.heappop(heap)
        derecho = heapq.heappop(heap)
        padre = Nodo(peso=izquierdo.peso + derecho.peso)
        padre.izquierdo = izquierdo
        padre.derecho = derecho
        izquierdo.padre = padre
        derecho.padre = padre
        heapq.heappush(heap, padre)
    
    return heap[0]

# Función para recorrer el árbol y extraer las frecuencias y pesos
def recorrer_arbol(nodo, frecuencias):
    if nodo.caracter:
        frecuencias[nodo.caracter] = nodo.peso
    if nodo.izquierdo:
        recorrer_arbol(nodo.izquierdo, frecuencias)
    if nodo.derecho:
        recorrer_arbol(nodo.derecho, frecuencias)

# Función para guardar los resultados en un archivo CSV
def guardar_csv(frecuencias, nombre_archivo='resultadosGallager.csv'):
    with open(nombre_archivo, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Caracter', 'Frecuencia'])
        for caracter, frecuencia in frecuencias.items():
            escritor.writerow([caracter, frecuencia])

# Función para graficar el árbol de Huffman verticalmente
def graficar_arbol(nodo):
    grafo = nx.DiGraph()
    etiquetas = {}
    agregar_nodo_al_grafo(nodo, grafo, etiquetas, '0')
    pos = jerarquia_posicion(grafo, '0')
    nx.draw(grafo, pos, with_labels=True, labels=etiquetas, node_size=2000, node_color='skyblue', font_size=10)
    plt.show()

def agregar_nodo_al_grafo(nodo, grafo, etiquetas, nombre):
    if nodo.caracter:
        etiquetas[nombre] = f'{nodo.caracter}:{nodo.peso}'
    else:
        etiquetas[nombre] = str(nodo.peso)
    
    if nodo.izquierdo:
        grafo.add_edge(nombre, nombre + '0')
        agregar_nodo_al_grafo(nodo.izquierdo, grafo, etiquetas, nombre + '0')
    if nodo.derecho:
        grafo.add_edge(nombre, nombre + '1')
        agregar_nodo_al_grafo(nodo.derecho, grafo, etiquetas, nombre + '1')

def jerarquia_posicion(grafo, root):
    pos = {}
    niveles = list(nx.bfs_layers(grafo, root))
    y = 0
    for nivel in niveles:
        x = 0
        for nodo in nivel:
            pos[nodo] = (x, y)
            x += 1
        y -= 1
    return pos

# Función principal
def main(texto):
    # Calcular frecuencias iniciales
    frecuencias = {}
    for caracter in texto:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    
    # Construir el árbol de Huffman
    raiz = construir_arbol_huffman(frecuencias)

    # Incrementar pesos según el método de Gallager
    for caracter in texto:
        nodo = buscar_nodo(raiz, caracter)
        incrementar_peso(nodo)

    # Extraer frecuencias finales
    frecuencias_finales = {}
    recorrer_arbol(raiz, frecuencias_finales)

    # Guardar resultados en un CSV
    guardar_csv(frecuencias_finales)

    # Graficar el árbol de Huffman
    graficar_arbol(raiz)

def buscar_nodo(nodo, caracter):
    if nodo.caracter == caracter:
        return nodo
    if nodo.izquierdo:
        resultado = buscar_nodo(nodo.izquierdo, caracter)
        if resultado:
            return resultado
    if nodo.derecho:
        resultado = buscar_nodo(nodo.derecho, caracter)
        if resultado:
            return resultado
    return None

# Leer el texto de entrada
texto = input("Ingrese el texto: ")
main(texto)


