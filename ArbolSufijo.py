import networkx as nx
import matplotlib.pyplot as plt

def dibujarArbol(ramas, n):
    G = nx.Graph()

    for i, nodos in enumerate(ramas):
        rama = f"Rama{i+1}"
        
        # Agregar los nodos de la rama al grafo principal y conectarlos entre sí
        for j in range(len(nodos)):
            nodo = nodos[j]
            G.add_node(nodo)
            if j > 0:
                G.add_edge(nodos[j-1], nodo)
            if j == len(nodos) - 1:
                G.add_edge(nodo, rama)  # Conectar el último nodo de la rama 

    nodos_iniciales = [nodos[0] for nodos in ramas]

    # Unir todas las ramas 
    for nodo_inicial in nodos_iniciales:
        G.add_edge(f"Nivel {n}", nodo_inicial)  # Suponiendo que hay un nodo de raíz al que se conectan todas las ramas

    # Eliminar rama identificadora 
    for i in range(1, len(ramas)+1):
        G.remove_node(f"Rama{i}")

    pos = nx.spring_layout(G) 
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=12, font_weight="bold")
    plt.show()

print("Árbol de sufijo")
texto = input("Ingresa el texto: ")

ramas = []
#Encontrar la cantidad de ramas
for caracter in texto:
    caracter
    if caracter not in ramas:
        ramas.append(caracter)

#Asignar nodos a ramas
arbol = []
for rama in ramas:
    comenzar = 0 
    valores_rama = []
    for caracter in texto:
        if caracter == rama:
            comenzar= 1
        if comenzar == 1:
            valores_rama.append(caracter)
        else:
            valores_rama.append("")
        
    arbol.append(valores_rama)

#Encontrar los niveles de las ramas
niveles = []
for n in range(0,len(texto)):
    nivel_completo = []
    nivel_completo_identificado = []
    identificador = 0
    for rama in arbol:
        i=0
        nivel = []
        nivel_identificar = []
        for caracter in rama:
            if i<=n:
                if(caracter!=""):
                    nivel.append(caracter)
                    nivel_identificar.append(f"   ' {caracter} '  {identificador}")
                    identificador+=1                    
            else:
                break
            i+=1
        if len(nivel)!=0:
            nivel_completo.append(nivel)
            nivel_completo_identificado.append(nivel_identificar)
    #Dibujar cada nivel
    niveles.append(nivel_completo)
    dibujarArbol(nivel_completo_identificado, n)

#Imprimir en consola los niveles
for i, nivel in enumerate(niveles, 1):
    print(f"Nivel {i}")
    print(nivel)
