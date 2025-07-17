import csv
import matplotlib.pyplot as plt
import networkx as nx

class Nodo:
    def __init__(self, simbolo=None, peso=1):
        self.simbolo = simbolo
        self.peso = peso
        self.izquierda = None
        self.derecha = None
        self.padre = None
        self.es_hoja = simbolo is not None

def contar_frecuencias(texto):
    frecuencias = {}
    for simbolo in texto:
        if simbolo in frecuencias:
            frecuencias[simbolo] += 1
        else:
            frecuencias[simbolo] = 1
    return frecuencias

def crear_arbol_inicial(frecuencias):
    nodos = [Nodo(simbolo=s, peso=frecuencias[s]) for s in frecuencias]
    for i in range(len(nodos) - 1):
        nodos[i].padre = nodos[i + 1]  # Ajuste para la relación padre-hijo
    return nodos

def encontrar_nodo(nodos, peso):
    for nodo in reversed(nodos):
        if nodo.peso == peso:
            return nodo
    return None

def incrementar_peso(nodo):
    actual = nodo
    while actual:
        actual.peso += 1
        actual = actual.padre

def algoritmo_knuth(arbol, simbolo):
    # Encontrar el nodo hoja correspondiente al símbolo
    nodo_hoja = None
    for nodo in arbol:
        if nodo.simbolo == simbolo:
            nodo_hoja = nodo
            break
    
    if not nodo_hoja:
        raise ValueError("Símbolo no encontrado en el árbol")
    
    # Intercambiar nodos
    actual = nodo_hoja
    while actual:
        # Encontrar el nodo más arriba con el mismo peso
        nodo_mismo_peso = encontrar_nodo(arbol, actual.peso)
        if nodo_mismo_peso:
            # Intercambiar actual y nodo_mismo_peso
            actual.simbolo, nodo_mismo_peso.simbolo = nodo_mismo_peso.simbolo, actual.simbolo
            actual.peso, nodo_mismo_peso.peso = nodo_mismo_peso.peso, actual.peso
        
        # Moverse al padre
        actual = actual.padre
    
    # Incrementar pesos
    incrementar_peso(nodo_hoja)

def imprimir_arbol(arbol):
    for nodo in arbol:
        print(f"Nodo símbolo: {nodo.simbolo}, peso: {nodo.peso}")

def guardar_arbol_en_csv(arbol, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['Símbolo', 'Peso'])
        for nodo in arbol:
            escritor_csv.writerow([nodo.simbolo, nodo.peso])

def dibujar_arbol(arbol):
    G = nx.DiGraph()
    
    for nodo in arbol:
        if nodo.padre:
            G.add_edge(nodo.padre.simbolo, nodo.simbolo, weight=nodo.peso)
    
    pos = nx.spring_layout(G)
    labels = {nodo.simbolo: f'{nodo.simbolo} ({nodo.peso})' for nodo in arbol}
    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', edge_color='gray')
    plt.title("Árbol de Huffman")
    plt.show()

# Leer el texto de entrada
texto = input("Ingrese el texto: ")

# Contar las frecuencias de los símbolos en el texto
frecuencias = contar_frecuencias(texto)

# Inicializar el árbol con símbolos y sus frecuencias
arbol = crear_arbol_inicial(frecuencias)

# Simular el escaneo de cada símbolo en el texto
for simbolo in texto:
    algoritmo_knuth(arbol, simbolo)

# Imprimir el árbol después de la actualización
imprimir_arbol(arbol)

# Guardar el árbol en un archivo CSV
nombre_archivo_csv = 'arbol_huffman.csv'
guardar_arbol_en_csv(arbol, nombre_archivo_csv)

print(f"El árbol de Huffman ha sido guardado en {nombre_archivo_csv}")

# Dibujar el árbol
dibujar_arbol(arbol)
